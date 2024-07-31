""" To obtain the code you've shared, here is an ideal prompt you could use:

---

"Hi ChatGPT, could you help me write a Python script for organizing files in a folder into subfolders based on their file extensions using Tkinter for the UI? The script should:

- Use a dictionary to map file extensions to their descriptions.
- Allow the user to select a folder using a Tkinter file dialog.
- Organize files into subfolders named after their extensions and descriptions.
- Ensure files with the same name are uniquely renamed in the destination folder.
- Display a message box with the number of files organized.
- Open the folder in the file explorer after organizing, with support for Windows, macOS, and Linux.

Please also include comments and follow good Python practices."

---

This prompt clearly outlines your requirements and expectations, enabling me to provide a tailored response effectively."""


import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import platform

# Dictionary to map file extensions to their descriptions (plural)
extension_descriptions = {
    'MP4': 'Videos',
    'MOV': 'Videos',
    'AVI': 'Videos',
    'MKV': 'Videos',
    'XLSX': 'Excel files',
    'XLS': 'Excel files',
    'DOCX': 'Word documents',
    'DOC': 'Word documents',
    'PDF': 'documents',
    'TXT': 'Text files',
    'JPEG': 'Images',
    'JPG': 'Images',
    'PNG': 'Images',
    'GIF': 'Images',
    'TIFF': 'Images',
    'PSD': 'Photoshop files',
    'AI': 'Illustrator files',
    'INDD': 'InDesign files',
    'EPUB': 'eBooks',
    'MOBI': 'eBooks',
    'MP3': 'Audio files',
    'WAV': 'Audio files',
    'FLAC': 'Audio files',
    'M4A': 'Audio files',
    'ZIP': 'Compressed files',
    'RAR': 'Compressed files',
    '7Z': 'Compressed files',
    'GZ': 'Compressed files',
    'DMG': 'Disk images',
    'ISO': 'Disk images',
    'APP': 'Applications',
    'PKG': 'Package files',
    'HTML': 'Web files',
    'CSS': 'Web files',
    'JS': 'JavaScript files',
    'PY': 'Python scripts',
    'RB': 'Ruby scripts',
    'JAVA': 'Java files',
    'C': 'C source files',
    'CPP': 'C++ source files',
    'H': 'Header files',
    'SWIFT': 'Swift files',
    'PLIST': 'Property list files',
    'SQL': 'SQL database files',
    'DB': 'Database files',
    'CSV': 'CSV files',
    'XML': 'XML files',
    'JSON': 'JSON files',
    # Add more mappings as needed
}

def organize_files_by_type(folder_path):
    # Counter for the number of files organized
    file_count = 0

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Get the full path of the file
        file_path = os.path.join(folder_path, filename)
        
        # Skip if it is a directory
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        
        # If there is no extension, skip the file
        if not file_extension:
            continue

        # Remove the dot from the file extension
        file_extension = file_extension[1:].upper()

        # Get the description for the file extension
        description = extension_descriptions.get(file_extension, 'Files')

        # Determine the subfolder path for this file type
        subfolder_name = f"{file_extension} {description}"
        subfolder_path = os.path.join(folder_path, subfolder_name)

        # Create the subfolder if it doesn't exist
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        
        # Determine the destination file path
        destination_path = os.path.join(subfolder_path, filename)

        # If the file already exists in the destination, create a unique name
        if os.path.exists(destination_path):
            base_name, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination_path):
                new_filename = f"{base_name}_{counter}{ext}"
                destination_path = os.path.join(subfolder_path, new_filename)
                counter += 1
        
        # Move the file to the subfolder
        shutil.move(file_path, destination_path)
        file_count += 1

    return file_count

def select_folder_and_organize():
    # Create the Tkinter root object
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select the folder
    folder_path = filedialog.askdirectory(title="Select Folder to Organize")
    
    if folder_path:
        file_count = organize_files_by_type(folder_path)
        messagebox.showinfo("Organize Files", f"Organized {file_count} files in {folder_path}")
        # Open the directory after organizing
        if platform.system() == "Windows":
            os.startfile(folder_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", folder_path])
        else:  # Linux
            subprocess.Popen(["xdg-open", folder_path])
    else:
        messagebox.showinfo("Organize Files", "No folder selected.")
    root.destroy()

if __name__ == "__main__":
    select_folder_and_organize()
