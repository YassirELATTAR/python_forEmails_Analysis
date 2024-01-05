"""
This script allows you to remove the automatic replies that your SMTP Gets.
There is another script in the creation that should analyze replies of customers using NLP libraries.
"""

import os
import re
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import time

#This functions lets you select the folder where you emails are saved.
def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Folder Where your emails are saved")
    return folder_path

#This functions lets you choose where to save the output file
def select_output_folder():
    root = tk.Tk()
    root.withdraw()
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    return output_folder


#Pattern of emails in retrived txt or eml files:
pattern = r'>([^<@\s]+@[^\s<]+)</'

# The folder containing .eml or .txt files
folder_path = select_folder()
# The desired output file directory
output_file = select_output_folder()


#This retrieves only failed recipients due to their unexistence:
def extract_failed_recipients(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

        # Conditions can be replaced depending on the SMTP error that you get
        if "wasn\'t found at" or "doesn\'t exist" or "it might not exist" or "unknown recipient" in content:
            # Use regex to find the recipient email addresses
            recipients = re.findall(pattern, content)
            if recipients:
                return recipients
    return None

##This functions saves the output of the previous function in a file:
def process_files(folder_path, output_file):
    print("Processing...")
    count =0
    today = datetime.now()
    formatted_date = today.strftime('%B%d').lower()
    output_file = os.path.join(output_file, f"BouncedEmailsResults_{formatted_date}.txt")
    with open(output_file, 'a') as output:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt') or filename.endswith('.eml'):
                #time.sleep(5)
                file_path = os.path.join(folder_path, filename)
                failed_recipients = extract_failed_recipients(file_path)

                if failed_recipients:
                    #Un-comment the following two lines if you want to see the counter in the terminal:
                    #count = count+1
                    #print(f"{count} emails have been found.")
                    output.write(f"{failed_recipients[0]}\n")
                    os.remove(file_path)
                    files = os.listdir(folder_path)
"""
                    if not bool(files):
                        print("sleeping...")
                        time.sleep(10)
                    else:
                        continue

"""
print("Zuerst, Lass uns die nicht verfügbaren E-Mails finden!")

process_files(folder_path, output_file)

#This function gets emails that are still valid, but they returned error due to OVER QUOTA
def extract_failed_recipients2(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

        if "quota exceeded" in content:
            recipients = re.findall(pattern, content)
            if recipients:
                return recipients
    return None



##This functions saves the output of the previous function in a file:
def process_files2(folder_path, output_file):
    count =0
    today = datetime.now()
    formatted_date = today.strftime('%B%d').lower()
    output_file = os.path.join(output_file, f"BouncedEmailsResults_{formatted_date}.txt")
    with open(output_file, 'a') as output:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt') or filename.endswith('.eml'):
                file_path = os.path.join(folder_path, filename)
                failed_recipients = extract_failed_recipients2(file_path)

                if failed_recipients:
                    #time.sleep(5)
                    #count = count+1
                    #print(f"{count} lines have been found.")
                    output.write(f"{failed_recipients[0]}\n")
                    os.remove(file_path)


print("Lass uns jetzt die E-Mails mit OVER-QUOTA finden!")

process_files2(folder_path, output_file)


