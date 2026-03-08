import psutil
import time
import os
import subprocess
from datetime import datetime

PROJECT_PATH = r"D:\THAT I CAN\automationa"
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

PROJECT_PATH = r"D:\THAT I CAN\automation" 
os.chdir(PROJECT_PATH)

subprocess.run(["git", "add", "."])

commit_message = "Auto commit " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

subprocess.run(["git", "commit", "-m", commit_message])

subprocess.run(["git", "push", "origin", "main"])

print("Push completed.")