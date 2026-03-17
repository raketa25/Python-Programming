"""
This code demonstrates how to use the os module in Python to work with directories and files. It retrieves the current directory, creates a file path, writes to a file, and reads from it.
1. The code first gets the directory of the current script using os.path.dirname(os.path.abspath(__file__)).
2. It then defines a file name and constructs the full file path using os.path.join().  
3. The code opens the file in write mode and writes a string to it.
4. Finally, it opens the file in read mode, reads the content, and prints it to the console. This demonstrates how to handle file paths and perform basic file operations using the os module in Python.

"""
import os

directory = os.path.dirname(os.path.abspath(__file__))

print(directory)

file_name = 'os-test.txt'

file_path = os.path.join(directory, file_name)

with open(file_path, 'w') as file:
    file.write('The OS Module is COOL')

with open(file_path, 'r') as file:
    message = file.read()

print(message)