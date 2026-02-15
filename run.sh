#!/bin/bash
# This script installs required dependencies and runs the launcher for the project.

set -e

# Install requirements (assuming a requirements.txt is present)
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found."
fi

# Run the launcher (assuming launcher.py is the entry point)
if [ -f "launcher.py" ]; then
    echo "Running the launcher..."
    python launcher.py
else
    echo "launcher.py not found."
fi
