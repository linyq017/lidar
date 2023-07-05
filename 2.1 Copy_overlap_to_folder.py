import os
import shutil

def copy_files_from_list(source_dir, destination_dir, file_list):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Read the file list and copy the files
    with open(file_list, "r") as file:
        for line in file:
            filename = line.strip()  # Remove any leading/trailing whitespaces or newline characters
            file_path = os.path.join(source_dir, filename)

            if os.path.isfile(file_path):
                shutil.copy(file_path, destination_dir)
            else:
                print(f"File '{filename}' not found in the source directory.")

    print("File copying completed.")
