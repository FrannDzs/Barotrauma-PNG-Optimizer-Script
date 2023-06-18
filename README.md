# Barotrauma PNG Optimizer Script

This Python script is designed to compress and resize PNG images within a folder and its subfolders using [pngquant](https://github.com/kornelski/pngquant) and [Pillow](https://pypi.org/project/Pillow/).

![Screenshot](https://i.imgur.com/ecFvVkr.png)

## Instructions

1. Download the repository and extract it to a location of your choice.

2. Download Python from [python.org](https://www.python.org/?downloads).

3. Install Python and make sure to check the "Add Python to PATH" option during installation.

4. Run the script `Barotrauma_PNG_optimizer.py` and follow the instructions.

## Features

- Automatically resizes images that exceed 4096 pixels in width or height while maintaining the aspect ratio, using the Lanczos algorithm.
- Rounds the image resolution to the nearest multiple of 4 to ensure correct internal compression within the game.
- Works by default with the mods installation folder: `%localappdata%\Daedalic Entertainment GmbH\Barotrauma\WorkshopMods\Installed`.
- Supports custom paths for image optimization.
- Displays file sizes before and after compression.
- Allows you to choose the quality range for optimization.
- Display a progress bar

## Dependencies

- [pip](https://pypi.org/project/pip/): It is automatically installed if the Python version is lower than 3.4.

- [Pillow](https://pypi.org/project/Pillow/): The script will prompt you to install it if necessary.

- [tqdm](https://pypi.org/project/tqdm/): It is automatically installed.

- [colorama](https://pypi.org/project/colorama/): It is automatically installed.
