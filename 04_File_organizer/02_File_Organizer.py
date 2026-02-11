# File Organiser (Mini-Project)

import os # importing os module to interact with the operating system
import shutil # importing shutil module to perform high-level file operations

# Folder path where files are located
FOLDER_PATH = "C:/Users/Amman/Downloads" # Change this to your target directory
os.chdir(FOLDER_PATH) # Change the current working directory to the specified folder path

# File Type Mapping
FILE_TYPES = { # Define file types and their corresponding extensions
    "PDFs": [".pdf"],
    "Word_Files": [".docx", ".doc"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Text_Files": [".txt"],
    "Installers": [".exe", ".msi", ".asc", ".msixbundle"],
    "Archives": [".zip", ".rar", ".7z"],
    "Torrents": [".torrent"],
    "Excel_Files": [".xlsx", ".xls", ".csv"],
    "PowerPoint_Files": [".pptx", ".ppt", ".odp"]
}


for folder in FILE_TYPES: # Create folders if they don't exist
    if not os.path.exists(folder): # Check if folder exists
        os.mkdir(folder)

for file in os.listdir(FOLDER_PATH): # Iterate through each file in the directory
    if file.startswith("."):
        continue # Skip hidden files (those starting with a dot)

    ext = os.path.splitext(file)[1].lower() # Get file extension and convert to lowercase

    for folder, extensions in FILE_TYPES.items(): # Check which folder the file belongs to
        if ext in extensions: # If the file extension matches
            shutil.move(file, os.path.join(folder, file)) # Move the file to the corresponding folder
            break
print(f"Organizing files in: {FOLDER_PATH}")
