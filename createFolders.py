import os
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime('%d%b')

# Define the main folder name
main_folder_name = f"{current_date}"

# Create the main folder
main_folder_path = os.path.join(os.getcwd(), main_folder_name)
os.makedirs(main_folder_path, exist_ok=True)

# List of subfolders
subfolders = ['Emma', 'Kate', 'David', 'Christine']

# Create subfolders inside the main folder
for subfolder in subfolders:
    subfolder_path = os.path.join(main_folder_path, subfolder)
    os.makedirs(subfolder_path, exist_ok=True)

print(f"Folder structure created in: {main_folder_path}")
