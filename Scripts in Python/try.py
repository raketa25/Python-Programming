"""
- This is a simple example of using try and except in Python. The code inside the try block will be executed, and if any error occurs, the code inside the except block will be executed instead. In this case, we are trying to print a message, and if it fails for some reason, we will print 'FAIL'. The pass statement is commented out, but it can be used to do nothing in the except block if you don't want to handle the error.
"""

message = "Hello students!"

try:
    print(message)
except:
    print('FAIL')
    #pass