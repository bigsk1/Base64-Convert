# Base64 Convert Images - Get txt file with base64 and a webp from jpg or png

## Overview

The Base64 Convert App is a Python script that automates the process of converting images to Base64 format and resizing them. It's particularly useful for embedding images directly into Markdown files for Jekyll-based websites. The app also generates WebP versions of the images for better compression and quality.

## Features

- Converts images in the `images` folder to Base64 format.
- Saves the Base64 string to a `.txt` file with the same name as the image.
- Resizes the image to 250x160 pixels. ( or the size you want, can be edited )
- Converts the resized image to WebP format.
- Saves the WebP image with a `_converted.webp` suffix.

## How to Use

1. **Setup**: Place the `convert.py` script in the same directory as your `images` folder.
2. **Batch File**: Double-click the provided `.bat` file. This will set up a Python virtual environment, install required packages, and run the `convert.py` script.
3. **Output**: After running, you'll find a `.txt` file containing the Base64 string and a `_converted.webp` image in the `images` folder for each image processed.

## Requirements

- Python 3.x
- Pillow library (automatically installed by the `.bat` file)

## Notes

- The `.bat` file will check if a virtual environment already exists. If it does, it will simply activate it and run the script.
- Detailed logs will be displayed in the CMD window, including any errors.

## Linux 

Use the convert.sh 

give it execute permissions (chmod +x convert.sh), and then you can run it with ./convert.sh
