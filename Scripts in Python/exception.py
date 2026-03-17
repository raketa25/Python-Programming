"""
- This is a simple example of using try, except, else, and finally in Python. The code inside the try block will be executed, and if any error occurs, the code inside the except block will be executed instead. In this case, we are trying to print a greeting message using the name provided by the user. If it fails for some reason (for example, if the input is not a string), we will print 'There was an error.' along with the error message. If there are no errors, the code inside the else block will be executed, which will print 'I'm happy to meet you!'. Finally, the code inside the finally block will always be executed, regardless of whether an error occurred or not. In this case, it will print 'The script is finished.' at the end of the script.

"""
name = input("Please enter your name:> ")

try:
    print(f'Hello {name}!')
except Exception as error:
    print(f'There was an error: {error}')
else:
    print('I\'m happy to meet you!')
finally:
    print('The script is finished.')