import os
import re
import time

def extract_failed_recipients(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

        # Check if the phrase "couldn't be delivered" is present in the content
        if "wasn\'t found at" or "doesn\'t exist" or "it might not exist" or " Message expired" or "unknown recipient" in content:
            # Use regex to find the recipient email addresses
            recipients = re.findall(r"message to (\S+@\S+) coul", content)
            
            if recipients:
                return recipients
    return None

def process_files(folder_path, output_file):
    count =0
    with open(output_file, 'a') as output:
        for filename in os.listdir(folder_path):
            if filename.endswith('.eml'):
                #time.sleep(5)
                file_path = os.path.join(folder_path, filename)
                failed_recipients = extract_failed_recipients(file_path)

                if failed_recipients:
                    count = count+1
                    print(f"{count} lines have been found.")
                    output.write(f"{failed_recipients[0]}\n")
                    os.remove(file_path)

# Replace 'folder_path' with the path to the folder containing .eml files
folder_path = 'C:/Users/Rickest/Desktop/Bounce/30Nov/Paver'
# Replace 'output.txt' with the desired output file name
output_file = 'C:/Users/Rickest/Desktop/Bounce/30Nov/PaverBounceNov29.txt'

process_files(folder_path, output_file)