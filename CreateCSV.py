# Script to create a CSV file with the file names, index, length, and their corresponding languages.

import os
import csv

folder_path = './dataset/train/wav_train'
csv_file = 'file_language.csv'

# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['index', 'fname', 'label', 'length'])  # Write the header row

    # Iterate through the files in the folder
    for index, filename in enumerate(os.listdir(folder_path)):
        file_path = os.path.join(folder_path, filename)
        
        # Extract the language from the file name
        if filename.startswith('es'):
            language = 'Spanish'
        elif filename.startswith('de'):
            language = 'German'
        elif filename.startswith('en'):
            language = 'English'
        else:
            language = 'Unknown'
        
        # Write the index, file name, length, and language to the CSV file
        writer.writerow([index, filename, language, f"{(int)(10)}"])
