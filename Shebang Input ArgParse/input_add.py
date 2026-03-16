"""
This program demonstrates how to take input from the user and perform addition on the input values. It first takes two numbers as input, then it adds them as strings (which results in concatenation) and finally it converts the inputs to integers and adds them to get the correct numerical result.
To run this script, save it to a file named `input_add.py`, and execute it from the terminal using Python.
Example usage:
$ python3 input_add.py
num1: 5
num2: 10
510
15

"""
num1 = input('num1: ')
num2 = input('num2: ')

answer1 = num1 + num2

answer2 = int(num1) + int(num2)

print(answer1)

print(answer2)