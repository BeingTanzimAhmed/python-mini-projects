# File Organizer (Mini Project)

## Overview

This project is a Python-based file organization utility that automatically categorizes files in a selected directory based on their file extensions.

The goal of this project was to practice practical file handling, OS interaction, and automation logic using core Python modules.

---

## Problem Statement

Folders such as "Downloads" often become cluttered with mixed file types over time. Manually sorting them is repetitive and inefficient.

This script automates the organization process by:
- Scanning all files in a target directory
- Identifying file extensions
- Moving files into appropriate categorized folders

---

## Technologies Used

- Python
- os module
- shutil module

---

## Features

- Automatically creates folders if they do not exist
- Case-insensitive extension matching
- Skips hidden files
- Uses dictionary-based mapping for clean logic
- Structured and readable implementation

---

## Supported File Categories

The script currently organizes files into the following categories:

- PDFs
- Word Files (.doc, .docx)
- Images (.jpg, .jpeg, .png)
- Videos (.mp4, .mkv)
- Text Files (.txt)
- Installers (.exe, .msi, etc.)
- Archives (.zip, .rar, .7z)
- Torrents
- Excel Files (.xls, .xlsx, .csv)
- PowerPoint Files (.ppt, .pptx, .odp)

The mapping can be extended easily by modifying the FILE_TYPES dictionary.

---

## How It Works

1. A dictionary maps folder names to file extensions.
2. The script ensures required folders exist.
3. It loops through all files in the target directory.
4. It extracts file extensions using os.path.splitext().
5. Matching files are moved using shutil.move().

---

## How to Run

1. Update the FOLDER_PATH variable inside the script:

   FOLDER_PATH = "C:/Users/YourName/Downloads"

2. Run the script:

   python 02_File_Organizer.py

3. Files will be organized automatically.

---

## Example

Before execution:
- report.pdf
- image.jpg
- data.csv
- setup.exe

After execution:
- PDFs/report.pdf
- Images/image.jpg
- Excel_Files/data.csv
- Installers/setup.exe

---

## Limitations

- Does not handle duplicate filenames
- No logging system implemented
- Works only at one directory level (non-recursive)
- No exception handling yet

---

## Future Improvements

- Add duplicate file handling
- Add error handling (try-except blocks)
- Add logging functionality
- Add recursive directory support
- Convert into a CLI tool with arguments

---

## Learning Outcome

This project helped reinforce:
- Practical file system manipulation
- Dictionary-based logic design
- Real-world automation scripting
- Writing structured and maintainable Python code
