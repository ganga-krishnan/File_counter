#!/usr/bin/env python
# coding: utf-8

# # Directory File Counter

# In[1]:


import os


# In[6]:


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

