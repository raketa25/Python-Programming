"""
This code demonstrates variable scope in Python. The variable `message` is defined in the global scope, and the function `bad_function` modifies a global variable `bad_var`. When `bad_function` is called, it prints the value of `message`, and after the function call, the value of `bad_var` is printed, showing that it has been modified globally.
"""
message = 'words are cool'

def bad_function():
    global bad_var
    bad_var = 'bob'
    print(message)

bad_function()
print('\n')
print(bad_var)