import os
import re

def search_files():
    for root, dirs, files in os.walk("C:/Users/Rickest/Desktop/Bounce/x679611"):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors='ignore') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        match = re.search(r'Your message to <span style=\"color:#0072c6\">(.+?)<\/span> couldn\'t be delivered.', line)
                        if match:
                            with open(f"tohhtadl.txt", "a") as output_file:
                                output_file.write(match.group(1) + "\n")
                                break

search_files()
