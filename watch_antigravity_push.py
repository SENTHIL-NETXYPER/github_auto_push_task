import psutil
import time
import os
import subprocess
from datetime import datetime

# Correct project folder
PROJECT_PATH = r"D:\THAT I CAN\automation"

# Process name of the software
PROCESS_NAME = "Antigravity.exe"

print("Monitoring AntiGravity...")

def is_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == PROCESS_NAME:
            return True
    return False

# Wait until AntiGravity starts
while not is_running():
    time.sleep(2)

print("AntiGravity detected.")

# Wait until it closes
while is_running():
    time.sleep(2)

print("AntiGravity closed. Pushing code to GitHub...")

# Move to project directory
os.chdir(PROJECT_PATH)

# Stage changes
subprocess.run(["git", "add", "."])

# Create commit message with timestamp
commit_message = "Auto commit " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Commit changes
subprocess.run(["git", "commit", "-m", commit_message])

# Push to GitHub
subprocess.run(["git", "push", "origin", "main"])

print("Push completed successfully.")

# Prevent terminal from closing immediately
input("Press Enter to exit...")