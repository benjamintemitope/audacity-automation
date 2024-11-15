# Audacity Automation Script

This Python script automates audio processing tasks using Audacity, applying effects and exporting files to both WAV and MP3 formats. The script launches Audacity, processes `.aup3` files in a specified directory, and applies effects such as normalization and compression. 

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)

## Requirements

- Python 3.8 or higher
- [psutil](https://pypi.org/project/psutil/) - for managing system processes.
- [pyaudacity](https://github.com/asweigart/pyaudacity/) - to interact with Audacity’s API for automation.

Ensure that [Audacity](https://www.audacityteam.org/) is installed on your system.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/benjamintemitope/audacity-automation.git
cd audacity-automation
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Configuration
- **AUDACITY_PATH**: Update this path to where Audacity is installed on your system.
- **LAUNCH_DELAY**: Time delay in seconds to ensure Audacity has launched before the script attempts to interact with it. Default is set to `3` seconds.

## Usage
To run the script, use the following command:
```bash
python script.py <directory>
```
- `<directory>`: The path to the folder containing `.aup3` files you want to process.

### Example
```bash
python script.py "C:\path\to\your\aup3\files"
```
The script will launch Audacity (if it’s not already running), process each .aup3 file in the specified directory, apply effects, and export the results as both WAV and MP3 files.

## Troubleshooting
- **Audacity Not Launching**: Verify that `AUDACITY_PATH` points to the correct installation path.
- **Missing Dependencies**: Install dependencies from `requirements.txt`.
- **Permissions Issues**: Run the script with administrative privileges if you encounter file access errors.
