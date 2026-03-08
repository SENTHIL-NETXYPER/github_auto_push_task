import subprocess
import os
from datetime import datetime

PROJECT_PATH = r"D:\THAT I CAN\automationa"
ANTIGRAVITY_PATH = r"D:\all files on downloards\Downloads\Antigravity.exe"

print("Starting AntiGravity...")

process = subprocess.Popen(ANTIGRAVITY_PATH)

print("Waiting for AntiGravity to close...")
process.wait()

print("Software closed. Pushing code to GitHub...")

os.chdir(PROJECT_PATH)

subprocess.run(["git", "add", "."])

commit_message = "Auto commit " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

subprocess.run(["git", "commit", "-m", commit_message])

subprocess.run(["git", "push", "origin", "main"])

print("Code pushed successfully.")