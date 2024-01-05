import os
import re

def search_files():
    for root, dirs, files in os.walk("C:/Users/Administrator/Desktop/DATA/x0d10zi/bounceofstorageappvault.store_20230522-2239/messages"):
        for file in files:
            if file.endswith(".eml"):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors='ignore') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        match = re.search(r'Your message to(.+?)couldn\'t be delivered.', line)
                        if match:
                            with open(r"ma8d.txt", "a") as output_file:
                                output_file.write(match.group(1) + "\n")
                                break

search_files()
