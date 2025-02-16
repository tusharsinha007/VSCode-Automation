import os
import time
import subprocess
import pyautogui
from datetime import datetime

VSCODE_PATH = r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe"
FOLDER_PATH = r"C:\Users\User\Desktop\leehntgjyiSDF4\Leetcoder"
TARGET_TIME = "13:13"  # Set your desired launch time (24-hour format)

def wait_for_time(target_time):
    """Waits until the specified time before proceeding."""
    print(f"⏳ Waiting until {target_time} to open VS Code...")
    
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == target_time:
            print(f"⏰ Time matched! Launching VS Code now...")
            break
        time.sleep(30)  # Check every 30 seconds

def open_vscode_and_run_command(folder_path):
    """Opens VS Code, launches the terminal, and runs a command using pyautogui."""
    try:
        # Open VS Code with the specified folder
        subprocess.Popen([VSCODE_PATH, folder_path], shell=True)
        print(f"✅ VSCode opened successfully with folder: {folder_path}")

        # Wait for VS Code to fully launch
        time.sleep(5)

        # Simulate keypress: Ctrl + ` (to open terminal)
        pyautogui.hotkey('ctrl', '`')
        print("✅ Terminal opened")

        # Wait for terminal to be ready
        time.sleep(2)

        # Type and execute the command
        pyautogui.write("node index.js")
        pyautogui.press("enter")
        print("✅ Executed: node index.js")

        # Wait and then send "1"
        time.sleep(2)
        pyautogui.write("1")
        pyautogui.press("enter")
        print("✅ Sent input: 1")

    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    wait_for_time(TARGET_TIME)
    open_vscode_and_run_command(FOLDER_PATH)

if __name__ == "__main__":
    main()
