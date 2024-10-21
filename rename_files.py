import os
import pandas as pd

# Load your CSV or Excel data
df = pd.read_csv(r'C:\Users\ncayo3\OneDrive - Georgia Institute of Technology\Documents\Documentation import.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Define the folder where the files are located
folder = r'C:\Users\ncayo3\OneDrive - Georgia Institute of Technology\Documents\SAM DOC DEMO'

# Loop through the document names and rename the files
for index, row in df.iterrows():
    old_name = str(row['Current Document Name'])  # Convert to string
    new_name = str(row['New Document Name'])      # Convert to string
    
    # Construct the full file paths
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)

    print(f"Attempting to rename: {old_name} -> {new_name}")

    # Rename the file if it exists
    if os.path.exists(old_path):
        try:
            os.rename(old_path, new_path)
            print(f'Successfully renamed: {old_name} -> {new_name}')
        except Exception as e:
            print(f'Error renaming {old_name}: {str(e)}')
    else:
        print(f'File not found: {old_name}')

print("Renaming process completed.")
