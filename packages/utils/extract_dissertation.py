# packages/utils/extract_dissertation.py
import os
import re
import pypdf

# Pre-formatted Markdown tables for Chapter 3
table_replacements = {
    "Table 3.1": """## Table 3.1: Data Requirements Mapped to Research Objectives

| Objective | Data Required | Data Type | Source |
|---|---|---|---|
| I — Identify heuristics | Responses on selection criteria, decision scenarios, institutional practices | Primary qualitative and quantitative | Questionnaire, PFA investment staff |
| II — Efficient frontier deviation | Property-level return and risk parameters; covariance matrix; optimal portfolio weights | Secondary/Synthetic | Calibrated synthetic universe; market publications for calibration |
| III — Comparative performance | Simulated return paths for both portfolios over 60-month horizon; six performance metrics | Synthetic/Computational | Monte Carlo simulation; GBM parameters from market index data |
| IV — Factors driving heuristics | Institutional, informational, and cognitive constraint data | Primary qualitative | Questionnaire Section D; open-ended responses |""",

    "Table 3.2": """## Table 3.2: Study Sampling Frame

| CPFA | Address |
|---|---|
| Nestle Nigeria Trust CPFA Limited | 22/24, Industrial Avenue, Ilupeju, Lagos. |
| Progress Trust CPFA Limited | No. 1, Abebe Village Road, Iganmu 101241, Lagos. |
| Shell Nigeria CPFA Limited | 21/22, Marina, Lagos. |
| Total Energies EP Nigeria CPFA Limited | Plot 35, Kofo Abayomi Street, Victoria Island, Lagos. |""",

    "Table 3.3": """## Table 3.3: Property Universe Geographic Distribution

| State | Submarket | Target Share |
|---|---|---|
| Lagos | Island (Ikoyi, VI, Lekki) | 25% |
| Lagos | Mainland (Ikeja GRA) | 15% |
| FCT, Abuja | Central (Maitama, Asokoro, Wuse II) | 20% |
| Rivers | Port Harcourt (GRA, Rumuola) | 18% |
| Kano | Bompai/Sharada Industrial | 12% |
| Oyo | Ibadan (Ring Road, Bodija Commercial) | 10% |""",

    "Table 3.4": """## Table 3.4: Property Universe Asset-type Distribution

| Asset Type | Target Share |
|---|---|
| Office Grade A/B | 28% |
| Commercial/Retail | 22% |
| Industrial/Logistics | 20% |
| Institutional Residential | 20% |
| Mixed-Use | 10% |""",

    "Table 3.5": """## Table 3.5: Property Universe Title Status Distribution

| Title Status | Target Share | Risk Premium |
|---|---|---|
| Certificate of Occupancy | 45% | 0.0% |
| Governor’s Consent | 25% | 0.5% |
| Gazette | 15% | 3.0% |
| Excision | 10% | 5.0% |
| Deed of Assignment | 5% | 2.0% |""",

    "Table 3.6": """## Table 3.6: Property Universe Price Range Distribution

| Tiers | Price Range (₦) | Target Share |
|---|---|---|
| Accessible | 150M - 350M | 20% |
| Core | 350M - 800M | 45% |
| Premium | 800M - 1.5B | 25% |
| Trophy | 1.5B - 3B | 10% |""",

    "Table 3.7": """## Table 3.7: Property Universe Condition Distribution

| Condition | Target Share |
|---|---|
| New | 20% |
| Good | 50% |
| Fair | 20% |
| Needs Renovation | 10% |""",

    "Table 3.8": """## Table 3.8: Performance Metric Calculation

| # | Metric | Formula | Variables Defined |
|---|---|---|---|
| M1 | Cumulative Return | $CR = \\frac{V_P(60)}{V_P(0)} - 1$ | V_P(0) = 1.0 (normalized); V_P(60) = terminal value |
| M2 | Annualized Return (CAGR) | $CAGR = (1 + CR)^{1/5} - 1$ | T = 5 years |
| M3 | Annualized Volatility | $\\sigma_P^{ann} = \\text{std}(\\{R_P(t)\\}_{t=1}^{60}) \\times \\sqrt{12}$ | Monthly returns annualized by √12 |
| M4 | Sharpe Ratio | $SR_P = \\frac{CAGR - R_f}{\\sigma_P^{ann}}$ | R_f = 0.15 |
| M5 | Maximum Drawdown | $MDD = \\max_{0 \\leq t \\leq 60} \\frac{V_{peak}(t) - V_P(t)}{V_{peak}(t)}$ | V_peak(t) = running maximum of portfolio value up to month t |
| M6 | Diversification Ratio | $DR = \\frac{\\sum_{i} w_i x_i \\sigma_i}{\\sigma_P^{ann}}$ | Weighted avg individual vol / portfolio vol; higher = better diversification |"""
}

def replace_page_tables(text, page_num):
    # Perform raw page-level replacements of tables to preserve content and prevent duplications
    if page_num == 44:
        pattern = r'Table\s*3\.1:.*?staff\b'
        text = re.sub(pattern, lambda m: table_replacements["Table 3.1"], text, flags=re.DOTALL | re.IGNORECASE)
    elif page_num == 45:
        pattern = r'Table\s*3\.2:.*?Directory\s*\(2026\)'
        text = re.sub(pattern, lambda m: table_replacements["Table 3.2"], text, flags=re.DOTALL | re.IGNORECASE)
    elif page_num == 47:
        pattern = r'Table\s*3\.3:.*?Research\s*\(2026\)'
        text = re.sub(pattern, lambda m: table_replacements["Table 3.3"], text, flags=re.DOTALL | re.IGNORECASE)
    elif page_num == 48:
        pattern_3_4 = r'Table\s*3\.4:.*?Research\s*\(2026\)'
        text = re.sub(pattern_3_4, lambda m: table_replacements["Table 3.4"], text, flags=re.DOTALL | re.IGNORECASE)
        pattern_3_5 = r'Table\s*3\.5:.*?Research\s*\(2026\)'
        text = re.sub(pattern_3_5, lambda m: table_replacements["Table 3.5"], text, flags=re.DOTALL | re.IGNORECASE)
    elif page_num == 49:
        pattern_3_6 = r'Table\s*3\.6:.*?Research\s*\(2026\)'
        text = re.sub(pattern_3_6, lambda m: table_replacements["Table 3.6"], text, flags=re.DOTALL | re.IGNORECASE)
        pattern_3_7 = r'Table\s*3\.7:.*?Research\s*\(2026\)'
        text = re.sub(pattern_3_7, lambda m: table_replacements["Table 3.7"], text, flags=re.DOTALL | re.IGNORECASE)
    elif page_num == 56:
        pattern_3_8 = r'Table\s*3\.8:.*?Variables\b'
        text = re.sub(pattern_3_8, lambda m: table_replacements["Table 3.8"], text, flags=re.DOTALL | re.IGNORECASE)
    elif page_num == 57:
        # Delete raw table rows of Table 3.8 on Page 57
        pattern_rows = r'\s*M1\s+Cumulative\s+Return.*?Source:\s+Author’s\s+Research\s+\(2026\)'
        text = re.sub(pattern_rows, '', text, flags=re.DOTALL | re.IGNORECASE)
    return text

def extract_clean_markdown(pdf_path, start_page, end_page, is_chapter3=False):
    reader = pypdf.PdfReader(pdf_path)
    pages_blocks = []
    
    for p in range(start_page - 1, end_page):
        page_num = p + 1
        text = reader.pages[p].extract_text(extraction_mode='layout')
        
        # Pre-process raw text for Chapter 3 tables
        if is_chapter3:
            text = replace_page_tables(text, page_num)
            
        # Split page by triple or more newlines (paragraph boundaries in layout mode)
        blocks = re.split(r'\n\s*\n\s*\n', text)
        cleaned_blocks = []
        
        for block in blocks:
            # Split block into lines separated by double newlines
            lines = [line.strip() for line in re.split(r'\n\s*\n', block) if line.strip()]
            if not lines:
                continue
                
            # Clean up double/multiple spaces
            cleaned_lines = [re.sub(r' {2,}', ' ', line) for line in lines]
            first_line = cleaned_lines[0]
            
            # Identify block type and format headings accordingly
            # Keep table and section titles intact (preserving rows separate)
            if first_line.startswith('## Table') or first_line.startswith('|') or first_line.startswith('# Table') or first_line.startswith('## SECTION') or first_line.startswith('# SECTION'):
                cleaned_block = '\n'.join(cleaned_lines)
            elif re.match(r'^(?:CHAPTER|APPENDIX)\b', first_line, re.IGNORECASE):
                cleaned_block = '# ' + '\n# '.join(cleaned_lines)
            elif first_line in ["INTRODUCTION", "REFERENCES", "PREAMBLE", "LITERATURE REVIEW", "RESEARCH METHODOLOGY", "QUESTIONNAIRE INSTRUMENT"]:
                cleaned_block = '# ' + first_line
            elif re.match(r'^\d+(?:\.\d+){2,}\b', first_line):
                cleaned_lines[0] = '### ' + first_line
                cleaned_block = '\n'.join(cleaned_lines)
            elif re.match(r'^\d+\.\d+\b', first_line):
                cleaned_lines[0] = '## ' + first_line
                cleaned_block = '\n'.join(cleaned_lines)
            else:
                cleaned_block = ' '.join(cleaned_lines)
                
            cleaned_blocks.append(cleaned_block)
            
        pages_blocks.append('\n\n'.join(cleaned_blocks))
        
    return '\n\n'.join(pages_blocks)

def insert_latex_equations(text):
    replacements = {
        r'\.+\s*Equation\s*3\.1\b': 
            r"""$$
ACS_k = \frac{w_1 \cdot B3_k + w_2 \cdot C1_k}{w_1 + w_2}
$$""",
        r'\.+\s*Equation\s*3\.2\b': 
            r"""$$
AVCS_k = \frac{w_1 \cdot B1\_rank\_loc_k + w_2 \cdot B2_k + w_3 \cdot C2_k}{w_1 + w_2 + w_3}
$$""",
        r'\.+\s*Equation\s*3\.3\b': 
            r"""$$
RCS_k = \frac{w_1 \cdot B1\_rank\_sector_k + w_2 \cdot C3_k}{w_1 + w_2}
$$""",
        r'\.+\s*Equation\s*3\.4\b': 
            r"""$$
HCS_k = \frac{w_1 \cdot B1\_rank\_peer_k + w_2 \cdot B4_k + w_3 \cdot C4_k}{w_1 + w_2 + w_3}
$$""",
        r'\.+\s*Equation\s*3\.5\b': 
            r"""$$
\bar{H}_j = \frac{1}{N} \sum_{k=1}^{N} H_{j,k}
$$""",
        r'\.+\s*Equation\s*3\.6\b': 
            r"""$$
\alpha_j = \frac{\bar{H}_j}{\sum_{i=1}^{4} \bar{H}_i}
$$""",
        r'Formula\s*3\.7:\s*Total\s*Acquisition\s*Cost\s*\(TAC\)\s*\.+\s*Equation\s*3\.7\b': 
            r"""### Formula 3.7: Total Acquisition Cost (TAC)
$$
TAC_i = P_i \times (1 + f_{agency} + f_{legal} + f_{consent,s_i})
$$""",
        r'Formula\s*3\.8:\s*Net\s*Operating\s*Income\s*\(NOI\)\s*\.+\s*Equation\s*3\.8\b': 
            r"""### Formula 3.8: Net Operating Income (NOI)
$$
NOI_i = (GR_i \times (1 - v_{a_i})) - (GR_i \times m_{a_i})
$$""",
        r'\.+\s*Equation\s*3\.9\b': 
            r"""$$
CR_i = \frac{NOI_i}{TAC_i}
$$""",
        r'\.+\s*Equation\s*3\.10\b': 
            r"""$$
E[R_i] = CR_i + \mu_{idx(i)}
$$""",
        r'\.+\s*Equation\s*3\.11\b': 
            r"""$$
\sigma_i = \sigma_{idx(i)} + \delta^{title}_{tl_i} + \delta^{cond}_{cn_i}
$$""",
        r'\.+\s*Equation\s*3\.12\b': 
            r"""$$
SR_i = \frac{E[R_i] - R_f}{\sigma_i}
$$""",
        r'Formula\s*3\.13:\s*Composite\s*Heuristic\s*Scoring\s*Function\s*\.+\s*Equation\s*3\.13\b': 
            r"""### Formula 3.13: Composite Heuristic Scoring Function
$$
H(p_i) = \alpha_1 \cdot TS(p_i) + \alpha_2 \cdot LS(p_i) + \alpha_3 \cdot MS(p_i) + \alpha_4 \cdot PS(p_i)
$$""",
        r'\.+\s*Equation\s*3\.14\b': 
            r"""$$
E[R_P] = \sum_{i=1}^{80} w_i x_i E[R_i] \quad \text{where} \quad w_i = \frac{1}{\sum_{j=1}^{80} x_j}
$$
$$
\sigma_P = \sqrt{\mathbf{x}^T \boldsymbol{\Sigma} \mathbf{x}} \quad \text{where} \quad \mathbf{x} \text{ is the vector of } x_i w_i
$$""",
        r'\.+\s*Equation\s*3\.15\b': 
            r"""$$
t = \frac{\bar{d}}{s_d / \sqrt{n}}
$$"""
    }
    
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, lambda m, r=replacement: r, text)
        
    return text

def extract_references_markdown(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    ref_lines = []
    
    for p in range(58, 65): # Pages 59-65
        text = reader.pages[p].extract_text(extraction_mode='layout')
        lines = text.split('\n')
        for line in lines:
            line_str = line.strip()
            if not line_str:
                continue
            line_str = re.sub(r' {2,}', ' ', line_str)
            if line_str == "REFERENCES":
                ref_lines.append("# REFERENCES\n")
                continue
            
            # Check if line had leading indentation in raw text layout
            has_leading = line.startswith(' ') or line.startswith('\t')
            if has_leading and ref_lines and not ref_lines[-1].endswith('\n'):
                ref_lines[-1] = ref_lines[-1] + " " + line_str
            else:
                if ref_lines and not ref_lines[-1].endswith('\n'):
                    ref_lines[-1] = ref_lines[-1] + "\n"
                ref_lines.append(line_str)
                
    if ref_lines and not ref_lines[-1].endswith('\n'):
        ref_lines[-1] = ref_lines[-1] + "\n"
        
    return '\n'.join(ref_lines)

def extract_clean_appendix(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    pages_text = []
    for p in range(65, 77): # Pages 66-77
        text = reader.pages[p].extract_text(extraction_mode='layout')
        pages_text.append(text)
    full_text = '\n\n'.join(pages_text)
    
    def replace_section(match):
        title = match.group(1).strip()
        title = re.sub(r'\s+', ' ', title)
        letter = match.group(2).strip()
        return f'\n\n## SECTION {letter}: {title}\n\n'
        
    full_text = re.sub(r'SECTION\s+([A-Za-z\s]+?)\n\s*([A-D])\b', replace_section, full_text)
    full_text = re.sub(r' (?=(?:○\s+[A-Z]))', '\n', full_text)
    
    blocks = re.split(r'\n\s*\n', full_text)
    cleaned_blocks = []
    for block in blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if not lines:
            continue
        cleaned_lines = [re.sub(r' {2,}', ' ', line) for line in lines]
        first_line = cleaned_lines[0]
        
        if re.match(r'^(?:APPENDIX|QUESTIONNAIRE|HEURISTICS)', first_line, re.IGNORECASE):
            cleaned_block = '# ' + '\n# '.join(cleaned_lines)
        elif first_line.startswith('##') or first_line.startswith('#'):
            cleaned_block = '\n'.join(cleaned_lines)
        elif re.match(r'^(?:○|[A-D]\d+\.|Criterion|Location|Title|Rental|Tenant|Physical|Activity|The valuer|Scenario C)', first_line):
            cleaned_block = '\n'.join(cleaned_lines)
        else:
            cleaned_block = ' '.join(cleaned_lines)
            
        cleaned_blocks.append(cleaned_block)
        
    return '\n\n'.join(cleaned_blocks)

def main():
    pdf_path = "ESM 519_ Project Dissertation.pdf"
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Source PDF file '{pdf_path}' not found at workspace root.")
        
    # Chapter 1: Pages 5-13
    ch1_text = extract_clean_markdown(pdf_path, 5, 13)
    with open("dissertation/chapters/chapter_1.md", "w", encoding="utf-8") as f:
        f.write(ch1_text)
    print("Cleaned Chapter 1 written.")
    
    # Chapter 2: Pages 14-42
    ch2_text = extract_clean_markdown(pdf_path, 14, 42)
    with open("dissertation/chapters/chapter_2.md", "w", encoding="utf-8") as f:
        f.write(ch2_text)
    print("Cleaned Chapter 2 written.")
    
    # Chapter 3: Pages 43-58
    ch3_text = extract_clean_markdown(pdf_path, 43, 58, is_chapter3=True)
    ch3_text = insert_latex_equations(ch3_text)
    with open("dissertation/chapters/chapter_3.md", "w", encoding="utf-8") as f:
        f.write(ch3_text)
    print("Cleaned Chapter 3 written.")
    
    # References: Pages 59-65
    ref_text = extract_references_markdown(pdf_path)
    with open("dissertation/references.md", "w", encoding="utf-8") as f:
        f.write(ref_text)
    print("Cleaned References written.")
    
    # Appendix A: Pages 66-77
    app_text = extract_clean_appendix(pdf_path)
    with open("dissertation/appendices/appendix_a.md", "w", encoding="utf-8") as f:
        f.write(app_text)
    print("Cleaned Appendix A written.")

if __name__ == "__main__":
    main()
