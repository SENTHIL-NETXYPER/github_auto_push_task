import os

def check_something():
    """Checks if a specific file exists."""
    filename = "data.txt"
    if os.path.exists(filename):
        return f"Check Passed: {filename} exists."
    else:
        return f"Check Failed: {filename} does not exist."

if __name__ == "__main__":
    # Execute the check
    result = check_something()
    print(result)
