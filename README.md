# Barotrauma PNG Optimizer Script

This Batch script is designed to compress PNG images within a folder and its subfolders using [pngquant](https://github.com/kornelski/pngquant)

## Instructions

1. Download the repository and extract it to a location of your choice.

2. Run the script `Barotrauma_PNG_Compressor.bat` and it will automatically compress the PNGs to 50-90 quality by replacing the original files in '%LocalAppData\Daedalic Entertainment GmbH\Barotrauma\WorkshopMods\Installed'

3. You can optionally round the images to the nearest multiple of 4 using `round_png.py`. Previously it was resized by limiting the resolution to 4096, but this causes the sprites to be misaligned. 
Rounding the images only changes by 1 pixel or 2, so there is no chance of the sprite being misaligned.
