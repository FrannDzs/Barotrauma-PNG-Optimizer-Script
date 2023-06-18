import os
import subprocess
from PIL import Image
import sys

def install_pip():
    if sys.version_info < (3, 4):
        print("pip not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
        print("pip installed successfully!")
    else:
        print("Python version is 3.4 or greater. Skipping pip installation.")

def install_pillow():
    try:
        import PIL
    except ImportError:
        print("Pillow not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
        print("Pillow installed successfully!")

def search_png_files(folder):
    png_files = []
    for path, directories, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".png"):
                png_files.append(os.path.join(path, file))
    return png_files

def execute_pngquant(file, quality):
    script_path = os.path.dirname(os.path.abspath(__file__))
    pngquant_path = os.path.join(script_path, "pngquant.exe")
    arguments = [pngquant_path, "--force", "--ext=.png", "--skip-if-larger", "--quality", quality, file]
    subprocess.run(arguments, shell=True)

def resize_images(file):
    img = Image.open(file)
    initial_size = img.size
    width, height = img.size
    max_dimension = max(width, height)
    
    if max_dimension > 4096:
        aspect_ratio = width / height
        if width > height:
            new_width = 4096
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = 4096
            new_width = int(new_height * aspect_ratio)
        
        new_width = round(new_width / 4) * 4
        new_height = round(new_height / 4) * 4
        
        img.thumbnail((new_width, new_height), Image.LANCZOS)
        img.save(file)
    
    resized_size = img.size
    return initial_size, resized_size

def print_header():
    print("\033[1;36m-------------------------------------------")
    print("\033[1;32mWelcome to the PNG file compression script for Barotrauma mods!")
    print("\033[1;34m===========================================")
    print("\033[1;32mThis script uses 'pngquant' to compress all .png files in a folder and its subfolders.")
    print("\033[1;32mCompressing PNG files can significantly reduce their size without loss of visual quality.")
    print("\033[1;32mBefore we begin, you will be asked whether you want to use the default path for the search folder. If you prefer to use a custom path, you will be able to enter it.")
    print("\033[1;32m- If you choose 'Y' (yes), default installation path of the mods will be used.")
    print("\033[1;33mNOTE: This can override all PNGs in the target.")
    print("\033[1;31m**I hope this script proves useful to you! If you have any questions, feel free to ask**")
    print("\033[1;36m--------------------------------------------")

def get_user_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please enter a valid option.")

def get_folder_path():
    use_default_url = get_user_input("\033[1mDo you want to use the default path? (%localappdata%\\Daedalic Entertainment GmbH\\Barotrauma\\WorkshopMods\\Installed)? (Y/N): ", ["y", "n"])
    if use_default_url == "y":
        return os.path.expandvars("%localappdata%\\Daedalic Entertainment GmbH\\Barotrauma\\WorkshopMods\\Installed")
    else:
        custom_folder = input("\033[1mEnter the custom folder address: ")
        proceed = get_user_input("\033[1mDo you wish to proceed with the address entered? (Y/N) ", ["y", "n"])
        if proceed == "y":
            return os.path.expandvars(custom_folder)
        else:
            print("\033[1mOperation canceled.")
            sys.exit()

def main():
    install_pip()
    install_pillow()
    print_header()
    input("\033[1mPress Enter to continue...")
    quality = input("\033[1mEnter the quality range (min-max) for compression: ")
    total_initial_size = 0
    total_compressed_size = 0

    valid_response = False
    while not valid_response:
        resize_option = get_user_input("\033[1mDo you want to automatically resize images larger than 4096x4096? (Y/N): ", ["y", "n"])
        if resize_option == 'y':
            print("\033[1;33mCAUTION: This will overwrite the original files...")
            valid_response = True
        elif resize_option == 'n':
            valid_response = True
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    search_folder = get_folder_path()
    found_files = search_png_files(search_folder)
    resized_files = []
    
    print("\033[1mPNG files found:")
    for file in found_files:
        print("\033[1m" + file)
        initial_size = os.path.getsize(file)
        execute_pngquant(file, quality)
        compressed_size = os.path.getsize(file)
        initial_resolution, resized_resolution = resize_images(file)
        print(f"\033[1mResolution before resizing: {initial_resolution}")
        print(f"\033[1mResolution after resizing: {resized_resolution}")
        print(f"\033[1mSize before compression: {initial_size} bytes")
        print(f"\033[1mSize after compression: {compressed_size} bytes")
        total_initial_size += initial_size
        total_compressed_size += compressed_size
        print("\033[1m-------------------------------------------")
        if initial_size != compressed_size or initial_resolution != resized_resolution:
            resized_files.append(file)
        print(f"\033[1mTotal size before compression: {total_initial_size} bytes")
        print(f"\033[1mTotal size after compression: {total_compressed_size} bytes")
        
if __name__ == "__main__":
    main()
