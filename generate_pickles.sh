#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Activate virtual environment if needed
# source /path/to/your/venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Additional setup commands if necessary
# echo "Running additional setup..."

# Function to process data in chunks
process_data_in_chunks() {
    batch_size=1000  # Adjust batch size as needed
    total_records=$(wc -l < data.csv)  # Example: Get total records (replace with actual data file)

    echo "Total records to process: $total_records"

    # Loop to process data in batches
    start=1
    while [ $start -le $total_records ]; do
        end=$((start + batch_size - 1))
        echo "Processing records $start to $end..."

        # Example: Process data in this range using process_data.py or any script
        python process_data.py --start $start --end $end

        # Check exit status
        if [ $? -ne 0 ]; then
            echo "Error: Data processing failed for records $start to $end."
            exit 1
        fi

        start=$((end + 1))
    done

    echo "Pickle generation completed successfully."
}

# Convert Jupyter notebook to Python script
echo "Converting Jupyter notebook to Python script..."
python -m nbconvert --to script Model.ipynb

# Check if conversion was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to convert Jupyter notebook to Python script."
    exit 1
fi

# Run the generated Python script
echo "Running the generated Python script..."
python Model.py

# Handle data processing in chunks
echo "Starting pickle generation process..."
process_data_in_chunks
