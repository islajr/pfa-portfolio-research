#!/bin/bash
# packages/generator/execute.sh
# Pipeline script to generate, calculate, validate, and freeze the property universe.

# Exit immediately if a command exits with a non-zero status
set -e

# Determine the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "=========================================================="
echo "RUNNING PROPERTY UNIVERSE GENERATION PIPELINE"
echo "=========================================================="

# Check if virtual environment exists at root and activate it, or use default python
if [ -f "../../.venv/bin/activate" ]; then
    echo "Activating root virtual environment..."
    source "../../.venv/bin/activate"
elif [ -f ".venv/bin/activate" ]; then
    echo "Activating local virtual environment..."
    source ".venv/bin/activate"
else
    echo "No virtual environment found, using system python..."
fi

# Ensure requirements are met (numpy, pandas, scipy, matplotlib, seaborn)
python3 -c "import numpy, pandas, scipy, matplotlib, seaborn" 2>/dev/null || {
    echo "Missing required packages. Installing..."
    pip install numpy pandas scipy matplotlib seaborn
}

echo "Step 1: Generating Raw Property Universe..."
python3 generate_universe.py

echo "Step 2: Calculating Financial Metrics..."
python3 metrics_calculator.py

echo "Step 3: Running Statistical Validation..."
python3 validate_universe.py

echo "Step 4: Freezing the Property Universe..."
python3 freeze_universe.py

echo "=========================================================="
echo "PIPELINE COMPLETED SUCCESSFULY ✓"
echo "=========================================================="
