"""Audacity Automation
By Benjamin Temitope <benjaminfranklin085@gmail.com>

This Python script automates audio processing tasks using Audacity, 
applying effects and exporting files to both WAV and MP3 formats. 

The script launches Audacity, processes `.aup3` files in a specified directory, 
and applies effects such as normalization and compression. 

"""

import os
import subprocess
import sys
import time
from pathlib import Path
from typing import List

import psutil
import pyaudacity as pa

# Constants
AUDACITY_PATH = Path(r"C:\Program Files\Audacity\Audacity.exe")
LAUNCH_DELAY = 3  # seconds

def is_audacity_running() -> bool:
    """Check if Audacity.exe is currently running."""
    return any(proc.info['name'] == 'Audacity.exe' for proc in psutil.process_iter(['name']))

def launch_audacity() -> None:
    """Launch Audacity if it's not already running."""
    if not is_audacity_running():
        print("Launching Audacity...")
        try:
            subprocess.Popen(AUDACITY_PATH)
        except FileNotFoundError:
            print(f"Error: Audacity executable not found at {AUDACITY_PATH}")
    else:
        print("Audacity is already running.")

def find_aup3_files(directory: str) -> List[str]:
    """
    Finds .aup3 files in the specified directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        List[str]: List of absolute paths to .aup3 files found in the directory.
    """
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise ValueError(f"The specified directory does not exist: {directory}")
    
    return [str(file_path.resolve()) for file_path in dir_path.glob("*.aup3")]

def apply_audio_effects_and_export() -> None:
    """
    Apply normalize and compressor effects, then export the audio to WAV and MP3.
    """
    pa.do('SelectAll')
    pa.do('Normalize:ApplyGain="1" PeakLevel="-1" RemoveDcOffset="1" StereoIndependent="0"')
    pa.do('Compressor:AttackTime="0.1" NoiseFloor="-60" Normalize="1" Ratio="3" ReleaseTime="1" Threshold="-20" UsePeak="0"')
    pa.do('LegacyMacroOutputFolder:Use_Preset="<Factory Defaults>"')
    pa.do('ExportWav')
    pa.do('ExportMp3')

def process_files_in_directory(directory: str) -> None:
    """
    Opens each .aup3 file in the specified directory, applies audio effects, and exports to WAV and MP3.

    Args:
        directory (str): Path to the directory containing .aup3 files.
    """
    aup3_files = find_aup3_files(directory)
    total_files = len(aup3_files)

    for index, file_path in enumerate(aup3_files, start=1):
        print(f"[{index}/{total_files}] Opening {Path(file_path).name}...")
        try:
            pa.open(file_path, True)
            apply_audio_effects_and_export()
        finally:
            pa.do('Close')

    print(f"Successfully exported {total_files} .aup3 files from {directory}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    launch_audacity()
    time.sleep(LAUNCH_DELAY)
    process_files_in_directory(target_directory)