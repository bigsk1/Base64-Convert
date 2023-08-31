#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install Pillow
echo "Installing Pillow..."
pip install Pillow

# Run the convert.py script
echo "Running convert.py..."
python convert.py

# Keep the terminal open
echo "Press any key to continue . . ."
read -n 1
