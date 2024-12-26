import os
import json

config_name="./config.json"

def get_path_from_config(config_name):
    with open(config_name, "r") as file:
        data = json.load(file)
    return data["Path"]

def list_files_in_path(path):
    try:
        # Get list of all files and directories in the given path
        items = os.listdir(path)

        # Filter the list to include only files
        files = [item for item in items if os.path.isfile(os.path.join(path, item))]

        return files
    except FileNotFoundError:
        print(f"The path '{path}' does not exist.")
        return []
    except PermissionError:
        print(f"Permission denied to access the path '{path}'.")
        return []
    
def moveFileToFolder(fileName):
    folder_mapping = {
        ".txt": "TextFiles",
        ".jpg": "Images",
        ".png": "Images",
        ".pdf": "Documents",
        ".docx": "Documents",
        ".c": "C Class",
        ".h": "C Class",
        ".java": "Java Class",
        ".jar": "Java Class",
        ".tar": "Zips",
        ".zip": "Zips",
        ".rar": "Zips",
        ".exe": "Exec",
        ".msi":"Exec"
        # Add more mappings as needed
    }

    # Get the file extension
    _, file_extension = os.path.splitext(fileName)

    # Determine the target folder based on the file extension
    target_folder = folder_mapping.get(file_extension, "Others")

    # Create the target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Construct the source and destination paths
    source_path = os.path.join(path, fileName)
    destination_path = os.path.join(target_folder, fileName)

    # except program files
    if fileName == "main.py" or fileName == "config.json":
        return

    # Move the file to the target folder
    try:
        os.rename(source_path, destination_path)
        print(f"Moved '{fileName}' to '{target_folder}'")
    except FileNotFoundError:
        print(f"The file '{fileName}' does not exist.")
    except PermissionError:
        print(f"Permission denied to move the file '{fileName}'.")
    except Exception as e:
        print(f"An error occurred while moving the file '{fileName}': {e}")


path = get_path_from_config(config_name)
while True:
    files = list_files_in_path(path)
    for file in files:
        moveFileToFolder(file)
