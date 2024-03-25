import os
import shutil
from tqdm import tqdm

def rename_heic_to_jpg(folder_path):
    # Get list of files in folder
    files = os.listdir(folder_path)
    # Filter out only HEIC files
    heic_files = [file for file in files if file.lower().endswith('.heic')]

    # If no HEIC files found, print a message and return
    if not heic_files:
        print("No HEIC files found in the specified folder.")
        return

    # Create a progress bar
    progress_bar = tqdm(total=len(heic_files), desc="Renaming files")

    # Rename each HEIC file to JPG
    renamed_count = 0
    for heic_file in heic_files:
        try:
            # Construct the paths for the source and destination files
            heic_file_path = os.path.join(folder_path, heic_file)
            jpg_file_path = os.path.join(folder_path, os.path.splitext(heic_file)[0] + '.jpg')
            
            # Rename the file
            shutil.move(heic_file_path, jpg_file_path)
            renamed_count += 1

            # Update progress bar description
            progress_bar.set_description(f"Renaming {heic_file}")
        except Exception as e:
            print(f"Error encountered while renaming {heic_file}: {e}")

        # Update progress bar
        progress_bar.update(1)

    # Close the progress bar
    progress_bar.close()

    # Print the number of files renamed
    print(f"Total {renamed_count} files renamed.")

# Example usage:
if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    rename_heic_to_jpg(folder_path)
