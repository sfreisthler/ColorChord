#!/bin/bash

# Check if 'venv' directory exists
if [ -d "venv" ]; then
    echo "Virtual environment already exists."
else
    # Create a virtual environment
    echo "Creating a virtual environment..."
    python3 -m venv venv

    # Check if venv was created successfully
    if [ $? -ne 0 ]; then
        echo "Error creating virtual environment. Exiting."
        exit 1
    fi
fi

# Activate the virtual environment
echo "Activating the virtual environment..."

# For macOS/Linux
source venv/bin/activate

# Install project dependencies from requirements.txt (if it exists)
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependency installation."
fi
