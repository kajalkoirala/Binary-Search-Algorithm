import os
import mimetypes
import shutil

def file_organizer(directory):
    if not os.path.exists(directory):
        print(f"Error: {directory} does not exist.")
        return
    
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)

        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Guess MIME type based on the file extension
        mimetype, _ = mimetypes.guess_type(file)

        # Categorize based on MIME type
        if mimetype:
            category = mimetype.split('/')[0]  
        else:
            category = 'unknown'

        # Create the folder if it doesn't exist
        folder = os.path.join(directory, category)
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Move the file to the folder
        shutil.move(filepath, os.path.join(folder, file))
        print(f"Successfully moved {file} to the {category} folder.")

# Example usage with the actual directory path
directory_to_organize = r"C:\Users\kajal\OneDrive\Desktop\Backend Development\Intermediate Python Projects"
file_organizer(directory_to_organize)
