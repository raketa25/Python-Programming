"""
This program demonstrates how to sanitize strings by replacing specific characters. It takes a name that contains double quotes, prints it, then replaces the double quotes with a different string and prints the sanitized version.

"""
name = '"Bob"'
print(name)

name = name.replace('"', '---')
print(name)