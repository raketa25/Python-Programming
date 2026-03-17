"""
This code demonstrates how to use the os module in Python to perform basic file system operations. It includes creating a directory, renaming it, and removing it. Additionally, it uses os.scandir() to list the contents of the current directory. The code is currently set to create a directory named 'test-dir', but the lines for renaming and removing the directory are commented out. You can uncomment those lines to see how they work. Finally, it prints the entries in the current directory using os.scandir().

"""

import os

# os.mkdir('test-dir')                     # Creates a directory named 'test-dir' in the current working directory. If the directory already exists, it will raise a FileExistsError.

# os.rename('test-dir', 'not-test-dir')     # Renames the directory 'test-dir' to 'not-test-dir'. If 'test-dir' does not exist, it will raise a FileNotFoundError. If 'not-test-dir' already exists, it will raise a FileExistsError. 

# os.rmdir('not-test-dir')                 # Removes the directory named 'not-test-dir'. The directory must be empty to be removed. If 'not-test-dir' does not exist, it will raise a FileNotFoundError. If the directory is not empty, it will raise an OSError.

result = os.scandir()

for x in result:
    print(x)