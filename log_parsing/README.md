This folder holds the log parser code for ogranizing the raw Mavlink logs
The script expects the log to be in excel format (.xlsx file extension)

log_parser_jupyter.ipynb is a jupyter notebook that holds the script to visualize how the code is working for understanding purposes.

log_parser.py allows you to run the log parser in shell provinding the path to a raw Mavlink log as a command line argument:

usage: python .\log_parser.py <path to Mavlink log>