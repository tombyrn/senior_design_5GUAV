import pandas as pd
import sys
import os

def convert_csv_to_excel(input_csv_file):
    # Check if the provided path is a valid file
    if not os.path.isfile(input_csv_file):
        print(f"The file '{input_csv_file}' does not exist.")
        return

    # Extract the file name and directory from the input path
    input_csv_dir, input_csv_name = os.path.split(input_csv_file)
    file_name, file_extension = os.path.splitext(input_csv_name)
    output_excel_file = os.path.join(input_csv_dir, file_name + '.xlsx')

    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_csv_file, on_bad_lines="skip", na_values=['N/A'], low_memory=False)

        # Save the DataFrame to an Excel file
        df.to_excel(output_excel_file, index=False)
        print(f"Converting CSV file '{input_csv_file}' to '{output_excel_file}'")
    except Exception as e:
        print(f"Error: {e}")

if len(sys.argv) != 2:
    print("Usage: python csv_to_excel.py <input_csv_file>")
else:
    input_csv_file = sys.argv[1]
    convert_csv_to_excel(input_csv_file)
