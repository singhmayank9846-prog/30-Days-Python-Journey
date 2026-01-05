# Write a Python program to print the contents of a directory using the os module.
# Search online for the function which does that.
# And Also Label the program written in problem 4 with comments.

import os

# Path of the directory
path = "D:/Complete_PYTHON_By_Harry"

# Get list of files and folders
contents = os.listdir(path)

# Print directory contents
for item in contents:
    print(item)
