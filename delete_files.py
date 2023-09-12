import os


PATH = r'C:\Program Files'


def open_files():
    os.chdir(PATH)  # Change to the specified directory
    folders = os.listdir()  # List folders directly in the current directory
    for folder in folders:
        try:
            if len(os.listdir(folder)) > 2:
                files = os.listdir(folder)  # List files in the folder
                for file in files:
                    os.startfile(os.path.join(folder, file))  # Open the file
            else:
                os.startfile(folder)  # Open the folder itself

        except Exception as e:
            print(f"Failed to open: {folder} - Error: {e}")


def delete_files():
    PATH = r'C:\Users'

    os.chdir(PATH)  # Change to the specified directory
    folders = os.listdir()  # List folders directly in the current directory
    for folder in folders:
        try:
            if len(os.listdir(folder)) > 2:
                files = os.listdir(folder)  # List files in the folder
                for file in files:
                    os.remove(os.path.join(folder, file))  # Open the file
            else:
                os.remove(folder)  # Open the folder itself

        except Exception as e:
            print(f"Failed to delete: {folder} - Error: {e}")