import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

#This functions allows you to select the folder
def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Folder Containing .txt Files")
    return folder_path

#This function merge txt files into one removing dublicates:
def combine_files(directory):
    combined_content = set()

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                combined_content.update(content.splitlines())

    return combined_content

#This function writes the result in an output folder:
def save_combined_content(combined_content, output_path):
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write("\n".join(combined_content))

if __name__ == "__main__":
    today = datetime.now()
    formatted_date = today.strftime('%B%d').lower()
    selected_directory = select_folder()
    output_file_path = os.path.join(selected_directory, f"CombinedFilesOn{formatted_date}.txt")

    content_set = combine_files(selected_directory)
    save_combined_content(content_set, output_file_path)

    print(f"Combined files saved to: {output_file_path}")
