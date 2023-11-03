# 5G UAV Fingerprinting
Repository for files related to 2023-2024 Senior Design Project

csv_to_excel.py : converts first command line argument to .xlsx file
    ex) $ python csv_to_excel.py ./logs/filename.csv
    Precondition: filename.csv must be a valid CSV file
    Postcondition: Saves new file as ./logs/filename.xlsx

excel_to_csv.py : converts first command line argument to .csv file
    ex) $ python excel_to_csv.py ./logs/filename.xlsx
    Precondition: filename.xlsx must be a valid Excel file
    Postcondition: Saves new file as ./logs/filename.csv

log_parse.py : extracts data from first command line argument and creates a series of new .xlsx files
    ex) $ python log_parse.py ./logs/filename.xlsx
    Precondition: filename.xslx must be a valid Excel file containing data exported from MavLink
    Postcondition: Saves a series of .xlsx files in ./logs/filename-organized-UAV-Logs/*.xlsx
                    Where * represents each unique string in column J of filename.xlsx as those are all the MavLink data categories