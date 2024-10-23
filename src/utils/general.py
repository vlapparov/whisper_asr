import os


def create_folder(folder_path: str):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder {folder_path}")


def remove_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Removed file {filepath}")
    else:
        print(f"The file {filepath} does not exist")
