"""
- This is a simple script that takes user input and prints it back to the console.
- The `input()` function is used to prompt the user for input, and the entered message is stored in the variable `message`.
- The script then uses an f-string to format the output, displaying the message that the user entered.
- To run this script, save it to a file named `input_function.py`, and execute it from the terminal using Python.
Example usage:
$ python3 input_function.py
What is your message: Hello, World!
you said "Hello, World!"

"""
message = input('What is your message: ')

print(f'you said "{message}"')