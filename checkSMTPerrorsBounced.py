import os
import re
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import time

#This function allows you to select the folder you want to remove emails returned
#Due to a problem in the SMTP
def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select folder where your emails to be removed first")
    return folder_path


def check_file_contains_phrase(file_path, target_phrase):
    # Read the content of the file
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        file_content = file.read()
    # Check if the target phrase is present in the file content
    return target_phrase in file_content

def remove_files_with_phrase(folder_path, target_phrase):
    count =0
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".eml") or filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            if check_file_contains_phrase(file_path,target_phrase):
                # If yes, remove the file
                os.remove(file_path)
                count = count+1
                print(f"{target_phrase} - got to {count}.")


# Replace 'folder_path' with the path to the folder containing .eml or .txt files
folder_path = select_folder()

#List of errors that could happen due to an error in the SMTP:
#You can add more errors depending on your SMTP
listToCheck = ["daily limit" , "550 5.1.90" , "550 5.1.8"]
for condition in listToCheck:
    print(f"checking Error: {condition}")
    remove_files_with_phrase(folder_path,condition)

