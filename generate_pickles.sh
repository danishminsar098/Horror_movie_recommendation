#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Activate virtual environment if needed
# source /path/to/your/venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Additional setup commands if necessary
# echo "Running additional setup..."

# Convert Jupyter notebook to Python script
echo "Converting Jupyter notebook to Python script..."
python -m nbconvert --to script Model.ipynb

# Run the generated Python script
echo "Running the generated Python script..."
python Model.py

echo "Pickle files generated successfully."
