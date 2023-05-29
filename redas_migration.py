import os
import shutil

def transfer_files(source_dir, destination_dir):
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        files = os.listdir(source_dir)
        for file in files:
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)
            shutil.copy(source_path, destination_path)
            os.remove(source_path)

        print("Files transferred and deleted successfully!")
    except FileNotFoundError:
        print("Source directory not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage: transfer files from "C:\source" to "D:\destination"
source_directory = "/home/pul/Desktop/booklet_pics_3"
destination_directory = "/home/pul/Desktop/booklet_pics_4"

transfer_files(source_directory, destination_directory)
