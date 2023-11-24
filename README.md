## Task: Directory File Counter
**Background**:   
Create a Python script that counts the number of files in a specified directory (and its subdirectories) with a given file extension.   

**Requirements:**
* Accept a directory path and a file extension as input.
* Recursively count and print the total number of files with the specified extension in the directory and its subdirectories.
* Handle cases where the specified directory doesn't exist.

**Submission:**    
Submit your Python script along with a brief document explaining how to use it and any considerations you took into account.


### Code with explanation

1.  **Importing necessary module**
  
`import os`   
The OS is a module, that provides the facility to establish the interaction between the user and the operating system. Here we need output from the system, so first we import it.  

2.  **Define a function**

`def count_files_with_extension(directory, ext)`   
There are two arguments: ___directory___ and ___ext___. The directory takes the path to the directory and ext takes the file extension.

3. **Checking the existence of directory**

`if not os.path.exists(directory):`     
    `print(f"The directory '{directory}' does not exist.")`   
    `return`   
This ___if___ statement checks if the specified directory exists using ___os.path.exists()___. If the directory doesn't exist, it prints a message and returns from the function.

4. **set a variable to initialize count** 

`total_files = 0`   
This variable ___total_files___ is initialized to count the total number of files with the specified extension.

5. **Traverse the directories and subdirectories**

`for dirpath, dirnames, filenames in os.walk(directory):`   
    `for filename in filenames:`   
        `if filename.endswith(ext):`   
            `total_files += 1`   
The ___os.walk()___ function generates the file names in a directory tree by walking the tree either top-down or bottom-up. In this code, it traverses through the specified directory and its subdirectories.   
For each file found (filename), it checks if the file ends with the specified ext (file extension). If it does, it increments the ___total_files___ counter.  
    
6. **Print the count**

`print(f"Total files with extension '{ext}' in '{directory}' and its subdirectories: {total_files}")`   
Finally, this line prints the total count of files with the specified extension in the specified directory and its subdirectories. 
  
7. **Input**

`directory_path = input("Enter directory path: ")`   
`file_extension = input("Enter file extension (e.g., '.txt'): ")`

`count_files_with_extension(directory_path, file_extension) `  
This part of the code prompts the user to input the directory path and the file extension. Then, it calls the ___count_files_with_extension___ function with the provided inputs to perform the counting operation and display the result.
