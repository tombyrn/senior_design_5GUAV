import pandas as pd
import sys
import os

def convert_excel_to_csv(input_excel_file):
    # Check if the provided path is a valid file
    if not os.path.isfile(input_excel_file):
        print(f"The file '{input_excel_file}' does not exist.")
        return

    # Extract the file name and directory from the input path
    input_excel_dir, input_excel_name = os.path.split(input_excel_file)
    file_name, file_extension = os.path.splitext(input_excel_name)
    output_csv_file = os.path.join(input_excel_dir, file_name + '.csv')

    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(input_excel_file)

        # Save the DataFrame to a CSV file
        df.to_csv(output_csv_file, index=False)
        print(f"Excel file '{input_excel_file}' converted and saved as '{output_csv_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) != 2:
    print("Usage: python excel_to_csv.py <input_excel_file>")
else:
    input_excel_file = sys.argv[1]
    convert_excel_to_csv(input_excel_file)
