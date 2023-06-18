# Barotrauma PNG optimizer script
 A python script to compress and resizing PNG images inside a folder and its subfolders using [pngquant](https://github.com/kornelski/pngquant) and [pillow](https://pypi.org/project/Pillow/) 

![](https://i.imgur.com/ecFvVkr.png)

# Instructions
1. Download the repo and extract it wherever you like

2. Download Python from https://www.python.org/?downloads

3. Install Python by checking the add to PATH option

4. Run the script `Barotrauma_PNG_optimizer.py` and follow the instructions

# Features
- Automatically resizes images exceeding 4096 by height or width, while maintaining the aspect ratio, using the Lanczos algorithm.
- Rounds image resolution to the nearest multiple of 4 to be able to compress the images internally correctly by the game
- Works by default with mods installation folder: `%localappdata%\Daedalic Entertainment GmbH\Barotrauma\WorkshopMods\Installed`
- Works with custom paths
- Displays file sizes before and after compression
- Possibility to choose the quality range

# Dependancies
- [pip](https://pypi.org/project/pip/): It is automatically installed if the Python version is lower than 3.4

- [pillow](https://pypi.org/project/Pillow/): The script will ask you if you want to install it

- [tqdm](https://pypi.org/project/tqdm/): It is automatically installed
