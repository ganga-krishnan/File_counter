## Task: Directory File Counter
**Background**:   
Create a Python script that counts the number of files in a specified directory (and its subdirectories) with a given file extension.   

**Requirements:**
* Accept a directory path and a file extension as input.
* Recursively count and print the total number of files with the specified extension in the directory and its subdirectories.
* Handle cases where the specified directory doesn't exist.

**Submission:** Submit your Python script along with a brief document explaining how to use it and any considerations you took into account.



### Code with explanation

import os

def count_files_with_extension(directory, ext):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    total_files = 0
    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(ext):
                total_files += 1
    
    print(f"Total files with extension '{ext}' in '{directory}' and its subdirectories: {total_files}")


directory_path = input("Enter directory path: ")
file_extension = input("Enter file extension (e.g., '.txt'): ")

count_files_with_extension(directory_path, file_extension)
