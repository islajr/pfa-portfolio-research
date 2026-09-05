#!/bin/bash
# packages/optimizer/execute.sh
# Coordinates the execution of Phase 4 Computational Pipeline.

set -e # Exit immediately if a command exits with a non-zero status

# Determine script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/../.." &> /dev/null && pwd )"

# Activate virtual environment
PYTHON_BIN="$PROJECT_ROOT/.venv/bin/python"

if [ ! -f "$PYTHON_BIN" ]; then
    echo "Error: Python executable not found at $PYTHON_BIN. Setup virtual environment first."
    exit 1
fi

echo "============================================="
echo "Starting Phase 4 Computational Pipeline..."
echo "============================================="

echo "Step 1: Running Heuristic Selection Engine (Portfolio A)..."
"$PYTHON_BIN" "$SCRIPT_DIR/heuristic_engine.py"
echo "---------------------------------------------"

echo "Step 2: Generating Property Covariance Matrix..."
"$PYTHON_BIN" "$SCRIPT_DIR/covariance.py"
echo "---------------------------------------------"

echo "Step 3: Running MVO Optimizer (Portfolio B)..."
"$PYTHON_BIN" "$SCRIPT_DIR/mvo_optimizer.py"
echo "---------------------------------------------"

echo "Step 4: Running Monte Carlo Simulation (GBM)..."
"$PYTHON_BIN" "$SCRIPT_DIR/monte_carlo.py"
echo "---------------------------------------------"

echo "Step 5: Executing Performance Metrics & Statistical Tests..."
"$PYTHON_BIN" "$SCRIPT_DIR/statistical_tests.py"
echo "---------------------------------------------"

echo "Step 6: Generating Figures and LaTeX Tables..."
"$PYTHON_BIN" "$SCRIPT_DIR/generate_outputs.py"
echo "============================================="
echo "Phase 4 pipeline completed successfully!"
echo "============================================="
