#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Convert Jupyter notebook to a Python script
echo "Converting Jupyter notebook to Python script..."
python -m nbconvert --to script Model.ipynb

# Run the generated Python script
echo "Running the generated Python script..."
python Model.py

echo "Pickle files generated successfully."
