# Mass-File-Renaming-Script
This repository contains a Python script that rename files based on data from a CSV or Excel file. The script reads the old and new file names from a CSV file and renames files in a specified folder accordingly.

## Project Background

This project was created due to an assignment to rename over **5,000 files** for import purposes. The task involved exporting student data as a CSV and concatenating **student IDs** to the old document names in order to generate new document names. The script automates this renaming process by reading the old and new file names from a CSV file and renaming the documents accordingly.

## Features

- **CSV Input**: The script loads a CSV file that contains two columns: `Current Document Name` and `New Document Name`.
- **File Renaming**: It renames the files in a specified folder based on the provided names.
- **Bulk Renaming**: Designed to handle a large volume of files (5,000+).
- **Error Handling**: The script checks if files exist before renaming and handles any renaming errors.
- **Logs**: Prints out information on whether each file was successfully renamed or if any errors occurred.

## Requirements

- Python 3.x
- Pandas (`pip install pandas`)

## How to Use

1. **Prepare the CSV File**:
   - Create a CSV file with two columns: `Current Document Name` and `New Document Name`.
   - Each row should contain the old file name and the corresponding new file name, typically by concatenating student IDs to the original file names.

2. **Specify Folder Path**:
   - Update the script to point to the folder where your files are stored:
     ```python
     folder = r'C:\path\to\your\folder'
     ```

3. **Run the Script**:
   - Ensure the CSV file path is correctly specified in the script:
     ```python
     df = pd.read_csv(r'C:\path\to\your\csvfile.csv')
     ```
   - Run the Python script:
     ```bash
     python rename_files.py
     ```

4. **Output**:
   - The script will print the renaming status of each file. It will notify you if a file is not found or if an error occurs during the renaming process.
