#!/bin/bash

# Check if 'venv' is active
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Error: Virtual environment is not active. Please activate it first."
    exit 1
fi

# Update installed dependencies
echo "Updating dependencies..."
pip install --upgrade pip
pip freeze > requirements.txt

# Add updated requirements.txt to git
echo "Staging changes for git..."
git add requirements.txt

# Commit the changes
echo "Committing updated requirements.txt..."
git commit -m "Updated dependencies and regenerated requirements.txt"

# Push to GitHub
echo "Pushing changes to GitHub..."
git push origin main  # Change 'main' to your actual branch name if different

echo "Dependencies updated and pushed to GitHub!"
