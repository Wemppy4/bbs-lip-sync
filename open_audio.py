import os
import tkinter as tk
from tkinter import filedialog
import subprocess
import shutil
from typing import Optional

# Constants
SUPPORTED_AUDIO_FORMATS = [("Audio Files", "*.wav *.mp3 *.ogg *.flac")]
OUTPUT_AUDIO_NAME = "audio.wav"
CONVERTED_AUDIO_NAME = "converted_audio.wav"
AUDIO_PATH = "temp_audio/"

def select_audio_file() -> Optional[str]:
    """
    Opens a dialog window to select an audio file.
    Returns the path to the selected file or None if no file is selected.
    """
    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=SUPPORTED_AUDIO_FORMATS
    )
    return file_path if file_path else None

def copy_audio_file(source_path: str, destination_path: str) -> bool:
    """
    Copies an audio file from source_path to destination_path.
    Returns True if the copy is successful, otherwise False.
    """
    try:
        shutil.copy(source_path, destination_path)
        print(f"File saved as {destination_path}")
        return True
    except PermissionError:
        print("Error: No write permissions for the folder. Run the program as an administrator.")
    except Exception as e:
        print(f"Error copying the file: {e}")
    return False

def convert_audio_file(input_path: str, output_path: str) -> bool:
    """
    Converts an audio file using ffmpeg.
    Returns True if the conversion is successful, otherwise False.
    """
    command = [
        "ffmpeg", "-y", "-i", input_path,
        "-ac", "1", "-ar", "16000", "-sample_fmt", "s16",
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"File successfully converted and saved as {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("Error: ffmpeg is not installed. Install ffmpeg and add it to PATH.")
    return False

def select_and_convert_audio():
    """
    Main function for selecting and converting an audio file.
    """
    # Select a file
    file_path = select_audio_file()
    if not file_path:
        print("No file selected.")
        return

    # Copy the file
    output_path = os.path.join(os.getcwd(), AUDIO_PATH+OUTPUT_AUDIO_NAME)
    if not copy_audio_file(file_path, output_path):
        return

    # Convert the file
    converted_path = os.path.join(os.getcwd(), AUDIO_PATH+CONVERTED_AUDIO_NAME)
    convert_audio_file(output_path, converted_path)

def main():
    """
    Main program function.
    """
    # Create a GUI window
    root = tk.Tk()
    root.withdraw()  # Hide the main window since we only need the dialog

    # Call the file selection and conversion function
    select_and_convert_audio()

if __name__ == "__main__":
    main()