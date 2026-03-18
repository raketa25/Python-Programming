"""
This code defines a function `say_hi` that takes a single argument `name` and prints a greeting message. The function is then called with a variable `person` set to 'bob', and subsequently, it is called in a loop for each name in the list `people`. This demonstrates how to define and use functions with arguments in Python.
"""
def say_hi(name):
    print(f'Hello {name}')

person = 'bob'

say_hi(person)

people = ['bob', 'sue', 'tim', 'fred']

for person in people:
    say_hi(person)