import os
import subprocess
from PIL import Image
import sys


def install_pip():
    if sys.version_info < (3, 4):
        print("\033[0;32mpip not found. Installing...\033[0m")
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
        print("\033[0;32mpip installed successfully!\033[0m")
    else:
        print("\033[0;32mPython version is 3.4 or greater. Skipping pip installation.\033[0m")


def install_pillow():
    try:
        import PIL
    except ImportError:
        print("\033[0;32mPillow not found. Installing...\033[0m")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
        print("\033[0;32mPillow installed successfully!\033[0m")


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
    else:
        new_width = round(width / 4) * 4
        new_height = round(height / 4) * 4

        img = img.resize((new_width, new_height), Image.LANCZOS)
        img.save(file)

    resized_size = img.size
    return initial_size, resized_size


def print_header():
    print("-------------------------------------------")
    print("\033[0;36mWelcome to the PNG file compression script for Barotrauma mods!\033[0m")
    print("===========================================")
    print("\033[0;37mThis script uses 'pngquant' to compress all .png files in a folder and its subfolders\033[0m")
    print("\033[0;32m/Compressing PNG files can significantly reduce their size without loss of visual quality\\ \033[0m")
    print("\033[0;37mBefore we begin, you will be asked whether you want to use the default path for the search folder. If you prefer to use a custom path, you will be able to enter it.\033[0m")
    print("\033[0;37m- If you choose 'Y' (yes), default installation path of the mods will be used.\033[0m")
    print("\033[0;31mNOTE: This can override all PNGs in the target.\033[0m")
    print("\033[0;34m**I hope this script proves useful to you! If you have any questions, feel free to ask**\033[0m")
    print("--------------------------------------------")


def get_user_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("\033[0;31mInvalid input. Please enter a valid option\033[0m")


def get_folder_path():
    use_default_url = get_user_input("Do you want to use the default path? (%localappdata%\\Daedalic Entertainment GmbH\\Barotrauma\\WorkshopMods\\Installed)? (Y/N): ", ["y", "n"])
    if use_default_url == "y":
        return os.path.expandvars("%localappdata%\\Daedalic Entertainment GmbH\\Barotrauma\\WorkshopMods\\Installed")
    else:
        custom_folder = input("Enter the custom folder address: ")
        proceed = get_user_input("\033[0;33mDo you wish to proceed with the address entered? (Y/N) \033[0m", ["y", "n"])
        if proceed == "y":
            return os.path.expandvars(custom_folder)
        else:
            print("\033[0;31mOperation canceled\033[0m")
            sys.exit()


def main():
    install_pip()
    install_pillow()
    print_header()
    input("\033[0;32mPress Enter to continue...\033[0m")
    quality = input("Enter the quality range (min-max) for compression: ")
    total_initial_size = 0
    total_compressed_size = 0
    
    valid_response = False
    while not valid_response:
        resize_option = get_user_input("Do you want to automatically resize images larger than 4096x4096 and round the width and height to the nearest multiple of 4? (Y/N): ", ["y", "n"])
        if resize_option == 'y':
            print("\033[0;33mCAUTION: This will overwrite the original files...\033[0m")
            valid_response = True
        elif resize_option == 'n':
            valid_response = True
        else:
            print("\033[0;31mInvalid input. Please enter 'Y' or 'N'.\033[0m")

    search_folder = get_folder_path()
    found_files = search_png_files(search_folder)

    print("\033[0;32PNG files found:\033[0m")
    for file in found_files:
        try:
            print(file)
            initial_size = os.path.getsize(file)
            execute_pngquant(file, quality)
            compressed_size = os.path.getsize(file)
            total_initial_size += initial_size
            total_compressed_size += compressed_size
            initial_resolution, resized_resolution = resize_images(file)
            print(f"Resolution before resizing: {initial_resolution}")
            print(f"\033[0;32mResolution after resizing: {resized_resolution}")
            print(f"Size before process: {initial_size} bytes")
            print(f"\033[0;32mSize after process: {compressed_size} bytes")
            print("-------------------------------------------")
        except Exception as e:
            print(f"Error processing file: {file}")
            print(f"Error message: {str(e)}")
            continue
            
    print("-------------------------------------------")
    print(f"Total initial size: {total_initial_size} bytes")
    print(f"\033[0;32mTotal compressed size:\033[0m {total_compressed_size} \033[0;32mbytes\033[0m")


if __name__ == "__main__":
    main()
