"""
This code demonstrates how to use regular expressions in Python to search for a specific pattern in a string. In this case, we are looking for a password pattern that starts with "pas", followed by one or more lowercase letters, and ends with "rd". If the pattern is found in the message, it will print the message; otherwise, it will print "No Password".

"""
import re

message = 'my paswrd is 123456'

if re.search('pas[a-z]+rd', message):
    print(message)
else:
    print('No Password')