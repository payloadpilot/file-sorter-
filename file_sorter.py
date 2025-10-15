import os
import shutil

# Set the folder you want to organize
source_folder = "C:/Users/Adarsh/Downloads"  # Change this to your target folder

# Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".sh", ".bat"]
}

# Create folders and move files
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(source_folder, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} to {folder}")
                break
