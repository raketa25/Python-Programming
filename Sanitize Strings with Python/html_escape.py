"""
This program demonstrates how to sanitize strings by escaping HTML characters. It takes a user message that contains HTML tags, writes it to a file, then uses the html.escape function to sanitize the message and appends the sanitized version to the same file.

"""
import html

user_message = '<h1>Hello World!!!</h1><a href="http://cnn.com">Click ME</a>'

with open('sanitize.html', 'w') as file:
    file.write(user_message)
    file.write('<hr>')

sanitized_message = html.escape(user_message)

with open('sanitize.html', 'a') as file:
    file.write(sanitized_message)