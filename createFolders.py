"""
This script is very basic. It is supposed to create folders for each SMTP
so that you can save the files in the correct place.
It should be run in the directory where you want to create the main folder.
"""

import os
from datetime import datetime

# Get the current date and name the folder as this example: 01Dec
current_date = datetime.now().strftime('%d%b')

# Define the main folder name
main_folder_name = f"{current_date}"

# Create the main folder
main_folder_path = os.path.join(os.getcwd(), main_folder_name)
os.makedirs(main_folder_path, exist_ok=True)

# List of subfolders (SMTPS)
#Here you can add the SMTPs names
subfolders = ['SMTP1', 'SMTP2', 'SMTP3']

# Create subfolders inside the main folder
for subfolder in subfolders:
    subfolder_path = os.path.join(main_folder_path, subfolder)
    os.makedirs(subfolder_path, exist_ok=True)

print(f"Folder structure created in: {main_folder_path}")
