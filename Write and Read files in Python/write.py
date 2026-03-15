"""
- How to manipulate files in python is key to avoid some unwanted behavior of our code.
"""

# Creating and writing into a file
file = open('test.txt', 'w')
file.write('Hello from FIRST example')
file.close()

# This the best as safer way to do the same as above
with open('test2.txt', 'w') as file2:
    file2.write('Hello from the SECOND example')