import os
import shutil

path = input("Enter your path: ")

try:
    # Get the list of files in the specified directory
    files = os.listdir(path)

    for i in files:
        # Get the file name and extension
        filename, extension = os.path.splitext(i)
        
        # Skip directories
        if extension == "":
            continue
        
        extension_1 = extension[1:]  # Remove the leading dot from the extension
        folder_path = os.path.join(path, extension_1)  # Create the folder path

        # Check if the folder exists; if not, create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file to the appropriate folder
        shutil.move(os.path.join(path, i), os.path.join(folder_path, i))

    print("Files have been organized successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
