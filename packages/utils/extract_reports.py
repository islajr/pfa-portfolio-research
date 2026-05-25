import os
import glob
import json
import time
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import Literal

IndexCode = Literal[
    "LG_OFF_ISL", "LG_RET_ISL", "LG_IND_MLN", "LG_RES_PRM", 
    "AB_OFF_CEN", "AB_RET_CEN", "PH_COM_OIL", "KN_IND_NTH"
]

# Tailored for institutional/pension fund property selection metrics
class PropertyMarketData(BaseModel):
    index_code: IndexCode | None = Field(description="The index code that best matches the location and asset class described.")
    mapping_rationale: str | None = Field(description="Briefly explain why this index_code was chosen (e.g., 'Report discusses Ikoyi office yields').")
    year: int | None = Field(description="The specific year the data applies to (between 2018 and 2024).")
    capital_apprc: float | None = Field(description="Capital appreciation percentage. Express as a decimal (e.g., 0.05 for 5%).")
    rental_yield: float | None = Field(description="Rental yield percentage. Express as a decimal.")
    annual_return: float | None = Field(description="Total annual return (if explicitly stated, otherwise null).")
    data_source: str = Field(description="Name of the reporting institution (e.g., Knight Frank, CBRE, NBS)")

# Initialize client automatically
client = genai.Client()

INDEX_MAPPING_GUIDE = """
Use the following definitions to map report data to index_codes:
- LG_OFF_ISL: Lagos Island Office (VI, Ikoyi, Marina)
- LG_RET_ISL: Lagos Island Retail (VI, Lekki Phase 1)
- LG_IND_MLN: Lagos Mainland Industrial (Apapa, Oshodi, Ikeja Ind.)
- LG_RES_PRM: Lagos Premium Residential (Ikoyi, VI, Lekki Phase 1)
- AB_OFF_CEN: Abuja Central Office (Maitama, Asokoro, Wuse II)
- AB_RET_CEN: Abuja Central Retail (Wuse II, Garki, Jabi)
- PH_COM_OIL: Port Harcourt Commercial (GRA, Rumuola, Trans Amadi)
- KN_IND_NTH: Kano Industrial North (Bompai, Sharada)
"""

def process_pdf(file_path):
    print(f"Uploading {file_path}...")
    uploaded_file = None
    try:
        # Upload the pdf to Gemini's File API
        uploaded_file = client.files.upload(
            file=file_path, 
            config=types.UploadFileConfig(mime_type="application/pdf")
        )
        
        prompt = f"""
        Analyze this real estate market report comprehensively.
        
        {INDEX_MAPPING_GUIDE}
        
        Extract EVERY relevant metric defined in the schema for the years 2018-2024.
        Read any embedded charts, graphs, and tables to find the yield, capital appreciation, and annual returns.
        Map the locations and asset classes to the closest matching index_code based on the guide above.
        Return an EXHAUSTIVE LIST of all data points found in the document.
        If a specific metric is not present or implied for a location/year, return null for that field.
        """
        
        print(f"Extracting data from {file_path}...")
        
        # Using gemini-3.5-flash as requested for superior extraction and low noise
        response = client.models.generate_content(
            model="gemini-3.5-flash", 
            contents=[uploaded_file, prompt], 
            config=types.GenerateContentConfig(
                response_mime_type="application/json", 
                response_schema=list[PropertyMarketData], 
                temperature=0.1
            ),
        )
        
        return json.loads(response.text)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        raise e
    finally:
        # Ensure the file is cleaned up even if extraction fails
        if uploaded_file:
            try:
                client.files.delete(name=uploaded_file.name)
            except Exception as cleanup_error:
                print(f"Failed to clean up file {uploaded_file.name}: {cleanup_error}")

def run_batch():
    # Determine the project root dynamically to handle absolute paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    report_dir = os.path.join(project_root, "data", "market-reports")
    pdf_files = glob.glob(os.path.join(report_dir, "*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {report_dir}. Please place reports there and try again.")
        return

    output_dir = os.path.join(project_root, "data", "calibration")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "raw_extracted_market_data.json")

    # Load existing data to append to and to track progress
    all_extracted_data = []
    processed_files = set()
    if os.path.exists(output_file):
        try:
            with open(output_file, "r") as f:
                all_extracted_data = json.load(f)
            processed_files = set(pt.get("source_file") for pt in all_extracted_data)
            print(f"Resuming: {len(processed_files)} files already processed. {len(all_extracted_data)} total records loaded.")
        except Exception as e:
            print(f"Could not load existing file {output_file}: {e}. Starting fresh.")
    
    for i, pdf in enumerate(pdf_files):
        pdf_name = os.path.basename(pdf)
        
        # Skip files already in the dataset to avoid duplicates in resumed batches
        if pdf_name in processed_files:
            continue
            
        print(f"\nProcessing {i+1}/{len(pdf_files)}: {pdf_name}")
        
        # Simple retry loop for rate limits or transient errors
        retries = 3
        for attempt in range(retries):
            try:
                data_points = process_pdf(pdf)
                # Attach source reference to each extracted record
                for pt in data_points:
                    pt["source_file"] = pdf_name
                
                all_extracted_data.extend(data_points)
                processed_files.add(pdf_name)
                
                # SAVE AFTER EACH SUCCESSFUL FILE
                # This ensures we don't lose data if the script is interrupted or hits a hard limit
                with open(output_file, "w") as f:
                    json.dump(all_extracted_data, f, indent=2)
                
                print(f"Success: Extracted {len(data_points)} records. Total: {len(all_extracted_data)}")
                break
            except Exception as e:
                print(f"Attempt {attempt + 1} failed on {pdf_name}: {e}")
                if attempt < retries - 1:
                    print("Waiting 15 seconds before retrying...")
                    time.sleep(15)
                else:
                    print(f"Skipping {pdf_name} after {retries} failures.")
        
        # Sleep to respect rate limits (especially for large PDFs)
        if i < len(pdf_files) - 1:
            print("Cooling down for 10 seconds to respect API rate limits...")
            time.sleep(10)
            
    print(f"\nBatch complete. Final count: {len(all_extracted_data)} records across {len(processed_files)} files.")
    print(f"Data saved in {output_file}")

if __name__ == "__main__":
    run_batch()
