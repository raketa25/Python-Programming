"""
This program demonstrates how to sanitize strings by stripping unwanted characters. It takes a name with leading and trailing whitespace, prints it, then uses the strip method to remove the whitespace and prints the sanitized version. It also shows how to strip specific characters from a string, such as angle brackets and certain letters.

"""
name = '   bob  '
print(f'----{name}----')

name = name.strip()
print(f'----{name}----')

user_name = '<h1>bob</h1>'
print(user_name)

user_name = user_name.strip('<>')
print(user_name)

user_name = user_name.lstrip('h1')
print(user_name)

user_name = user_name.rstrip('h1')
print(user_name)