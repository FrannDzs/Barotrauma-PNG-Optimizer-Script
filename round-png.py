import os
from PIL import Image

def resize_png_files(folder_path, batch_size=10):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                file_list.append(file_path)

                if len(file_list) >= batch_size:
                    process_images(file_list)
                    file_list = []

    if file_list:
        process_images(file_list)

def process_images(file_list):
    for file_path in file_list:
        try:
            with Image.open(file_path) as image:
                width, height = image.size

                new_width = round(width / 4) * 4
                new_height = round(height / 4) * 4

                if width != new_width or height != new_height:
                    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
                    resized_image.save(file_path)
                    print(f"File '{os.path.basename(file_path)}' resized from {width}x{height} to {new_width}x{new_height}")
                else:
                    print(f"File '{os.path.basename(file_path)}' does not require resizing. Current size: {width}x{height}")
        except Exception as e:
            print(f"An error occurred while processing file '{os.path.basename(file_path)}': {str(e)}")

# Corrected folder path
folder_path = os.path.expandvars(r"%localappdata%\Daedalic Entertainment GmbH\Barotrauma\WorkshopMods\Installed")

resize_png_files(folder_path)
