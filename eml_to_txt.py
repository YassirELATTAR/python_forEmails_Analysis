import os

folder_path = "C:/Users/Rickest/Desktop/Bounce/Paver"  # Replace with the path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".eml"):
        old_path = os.path.join(folder_path, filename)
        new_filename = os.path.splitext(filename)[0] + ".txt"
        new_path = os.path.join(folder_path, new_filename)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} to {new_filename}")
