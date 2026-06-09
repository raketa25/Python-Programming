"""
This code demonstrates the use of the built-in function `map()` in Python, which applies a specified function to each item of an iterable (like a list) and returns an iterator. The example shows how to use `map()` with a regular function, a lambda function, and also how to achieve the same result using list comprehension. The code squares each number in the list `nums` and prints the results.
"""

# The map(): It applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator).
# Application
nums = [1, 5, 10, 15, 20, 25]

def square(x):
  result = x**2
  return result

squared_nums = map(square, nums)
print(list(squared_nums))
print("\n")

# Using the lambda function
squared_nums_lambda = map(lambda x: x**2, nums)
print(list(squared_nums_lambda))
print("\n")

# Using list comprehension
squared_nums_comprehension = [num**2 for num in nums]
print(squared_nums_comprehension)