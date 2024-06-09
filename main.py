import time
import os
import numpy as np
import pyscreenshot as ImageGrab
import schedule
from datetime import datetime

# Dictionary to store file paths and their creation times
file_paths = {}

def take_screenshot():
    print("taking screenshot")
    # Generating acceptable timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
    image_name = f"screenshot-{timestamp}"
    screenshot = ImageGrab.grab()

    # Where to save screenshot
    filepath = f"./screenshots/{image_name}.png"

    # Saving screenshot to selected file path
    screenshot.save(filepath)
    print(f"screenshot taken and saved at {filepath}")

    # Add the file path and timestamp to the dictionary
    file_paths[filepath] = datetime.now()

def delete_screenshot():
    current_time = datetime.now()
    # Create a list of files to delete
    files_to_delete = [path for path, timestamp in file_paths.items() if (current_time - timestamp).seconds >= 5]

    for file_path in files_to_delete:
        if os.path.exists(file_path):
            try:
                # Delete the file
                os.remove(file_path)
                print(f"File {file_path} has been deleted successfully.")
                # Remove the file path from the dictionary
                del file_paths[file_path]
            except Exception as e:
                print(f"An error occurred while trying to delete the file: {e}")
        else:
            print(f"The file {file_path} does not exist.")
            # Remove the file path from the dictionary
            del file_paths[file_path]

def main():
    schedule.every(1).seconds.do(take_screenshot)
    schedule.every(1).seconds.do(delete_screenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()