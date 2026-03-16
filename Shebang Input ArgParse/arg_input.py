"""
- This script demonstrates how to use the argparse module to handle command-line arguments.
- It defines two positional arguments, `num1` and `num2`, which are expected to be strings representing numbers.
- The script then prints the parsed arguments, performs string concatenation on the inputs, and finally converts them to integers to perform addition.
- To run this script, save it to a file named `arg_input.py`, and execute it from the terminal using Python, providing the required arguments.
Example usage:
$ python3 arg_input.py 5 10
Namespace(num1='5', num2='10')
510
15

"""
import argparse

parser = argparse.ArgumentParser(description="Add two numbers.")
parser.add_argument('num1', help='First number', type=str)
parser.add_argument('num2', help='Second number', type=str)
args = parser.parse_args()

print(args)
print('\n')

answer1 = args.first + args.second
print(answer1)
print('\n')

answer2 = int(args.first) + int(args.second)
print(answer2)