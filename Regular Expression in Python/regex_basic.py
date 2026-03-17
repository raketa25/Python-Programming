import re

"""
This code demonstrates the use of regular expressions in Python to find specific patterns in a given message. It uses the `re` module to search for patterns that match certain criteria, such as words that start and end with 'b' and contain specific characters in between. The code includes examples of using different regex patterns to find matches in the message string.
the patterns used in the code are:
1. `b.b`: This pattern matches any three-character string that starts with 'b', followed by any character, and ends with 'b'.
2. `b.*b`: This pattern matches any string that starts with 'b', followed by any characters (zero or more), and ends with 'b'. It is greedy, meaning it will match as much as possible.
3. `b.*?b`: This pattern is similar to the previous one but is non-greedy (or lazy), meaning it will match as little as possible while still satisfying the condition of starting and ending with 'b'.
4. `b\bb.*?b\b`: This pattern matches words that start and end with 'b' and are treated as whole words (using word boundaries `\b`).
5. `b[A-Za-z]+b`: This pattern matches words that start and end with 'b' and contain one or more letters (both uppercase and lowercase) in between.

"""

message = 'bob says bamb in a barn as a bat barks at a bub'
print(message)
print('\n')

pattern = r'b.b'
print(re.findall(pattern, message))

pattern = r'b.*b'
print(re.findall(pattern, message))

pattern = r'b.*?b'
print(re.findall(pattern, message))

pattern = r'b\bb.*?b\b'
print(re.findall(pattern, message))

pattern = r'b[A-Za-z]+b'
print(re.findall(pattern, message))