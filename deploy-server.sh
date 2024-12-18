#!/bin/bash

# Update package list
echo "Updating package list..."
apt update

# Install ffmpeg
echo "Installing ffmpeg..."
apt install -y ffmpeg

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r ../requirements.txt

echo "Setup completed successfully!"
