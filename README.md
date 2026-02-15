# Fortnite Account Puller - Setup Guide

## Overview
This is a cross-platform Fortnite Account Puller application that works on Mac and Windows. It provides a GUI to fetch account inventory and cosmetics data.

## Requirements
- Python 3.7 or higher
- pip (Python package manager)

## Installation Instructions

### For Mac

1. Open Terminal

2. Install Python (if not already installed)
   ```
   brew install python3
   ```

3. Clone or Download the Repository
   ```
   cd path/to/your/aa
   ```

4. Install Dependencies
   ```
   pip install -r requirements.txt
   ```

5. Run the Application
   ```
   python3 launcher.py
   ```

### For Windows

1. Open Command Prompt (Win + R, type cmd)

2. Install Python (if not already installed)
   - Download from python.org
   - During installation, check "Add Python to PATH"

3. Navigate to the Project Directory
   ```
   cd path\to\your\aa
   ```

4. Install Dependencies
   ```
   pip install -r requirements.txt
   ```

5. Run the Application
   ```
   python launcher.py
   ```

## Using the Application

1. Enter Account Info: Type a username or account ID
2. Select Lookup Type: Choose "Username" or "Account ID"
3. Click Buttons:
   - Fetch Account Data - Get general account information
   - Get Inventory - View inventory items
   - Get Cosmetics - View cosmetics collection

## Troubleshooting

### Python Not Found
- Mac: Try python3 instead of python
- Windows: Make sure Python was added to PATH during installation

### tkinter Error
- Mac: brew install python-tk
- Windows: Reinstall Python and select tkinter during installation

### Module Not Found Error
- Run: pip install -r requirements.txt again

## File Structure
aa/
├── launcher.py - Main GUI application
├── fortnite_account_puller.py - Core API module
├── example_usage.py - Example usage script
├── requirements.txt - Python dependencies
└── README.md - This file

## Features
✅ Cross-platform (Mac & Windows)
✅ User-friendly GUI
✅ Fetch account data by username or account ID
✅ Get inventory items
✅ Get cosmetics collection
✅ Error handling and validation

## Support
For issues or questions, please open a GitHub issue in this repository.
