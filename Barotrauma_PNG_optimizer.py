import os
import subprocess

def search_png_files(folder):
    png_files = []
    for path, directories, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".png"):
                full_path = os.path.join(path, file)
                png_files.append(full_path)
    return png_files

def execute_pngquant(file):
    script_path = os.path.dirname(os.path.abspath(__file__))
    pngquant_path = os.path.join(script_path, "pngquant.exe")
    arguments = [pngquant_path, "--force", "--ext=.png", "--skip-if-larger", "--quality", quality, file]
    subprocess.run(arguments, shell=True)

print("---------------------------------------------------------------------------------------------------------------------------------------")
print()
print("Welcome to the PNG file compression script for Barotrauma mods!")
print("===========================================")
print()
print("This script uses 'pngquant' to compress all .png files in a folder and its subfolders.")
print()
print("Compressing PNG files can significantly reduce their size without loss of visual quality.")
print()
print("Before we begin, you will be asked whether you want to use the default path for the search folder. If you prefer to use a custom path, you will be able to enter it.")
print()
print("- If you choose 'Y' (yes), default installation path of the mods will be used.")
print()
print("NOTE: This can override all PNGs in target. ")
print()
print("**I hope this script proves useful to you! If you have any questions, feel free to ask**")
print()
print("---------------------------------------------------------------------------------------------------------------------------------------")

# Prompt user input to continue
option = input("Press Enter to continue...")
quality = input("Enter the quality range (min-max) for compression: ")
    execute_pngquant(file, quality)

# Ask the user if he/she wants to use the default path
valid_response = False
while not valid_response:
    use_default_url = input("Do you want to use the default path? (%localappdata%\\Daedalic Entertainment GmbH\\Barotrauma\\WorkshopMods\\Installed)? (Y/N): ")
    use_default_url = use_default_url.lower()
    if use_default_url == "y" or use_default_url == "n":
        valid_response = True
    else:
        print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

if use_default_url == "y":
    print("CAUTION: This will overwrite the original files...")
    option = input("Press Enter to continue...")
    search_folder = os.path.expandvars("%localappdata%\\Daedalic Entertainment GmbH\\Barotrauma\\WorkshopMods\\Installed")
else:
    # Ask the user to enter a custom address
    custom_folder = input("Enter the custom folder address: ")
    proceed = input("Do you wish to proceed with the address entered? (Y/N) ")

    valid_response = False
    while not valid_response:
        if proceed.lower() == "y":
            print("CAUTION: This will overwrite the original files...")
            option = input("Press Enter to continue...")
            valid_response = True
        elif proceed.lower() == "n":
            print("Operation canceled.")
            exit()
        else:
            proceed = input("Invalid input. Please enter 'Y' for yes or 'N' for no.")

    search_folder = os.path.expandvars(custom_folder)

found_files = search_png_files(search_folder)

print("PNG files found:")
for file in found_files:
    print(file)
    initial_size = os.path.getsize(file)
    execute_pngquant(file)
    compressed_size = os.path.getsize(file)
    print(f"Size before compression: {initial_size} bytes")
    print(f"Size after compression: {compressed_size} bytes")
