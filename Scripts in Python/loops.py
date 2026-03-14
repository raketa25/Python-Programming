"""
Loops in Python are used to execute a block of code repeatedly until a certain condition is met. There are two main types of loops in Python: while loops and for loops.
- While loops : A while loop continues to execute a block of code as long as a specified condition is true. The syntax for a while loop is as follows:
while condition:
    # code to be executed
- For loops : A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object. The syntax for a for loop is as follows:
for variable in sequence:
    # code to be executed
In addition to these basic loop structures, Python also provides control statements such as break and continue that can be used to alter the flow of the loop. The break statement is used to exit a loop prematurely, while the continue statement is used to skip the current iteration and move on to the next one. Loops are an essential part of programming and are used in a wide variety of applications, from data processing to web development and beyond. Understanding how to use loops effectively is crucial for any Python programmer, and it can help you write more efficient and powerful code. By mastering loops in Python, you can take your programming skills to the next level and create more complex and sophisticated applications. So, whether you're a beginner or an experienced programmer, learning how to use loops in Python is an important step in your programming journey.

Note: Never use a while loop in an API call, as it can lead to infinite loops and cause the API to crash. Always make sure to include a condition that will eventually be met to exit the loop, or consider using a for loop instead if you need to iterate over a specific number of items. Additionally, be cautious when using loops in any code that interacts with external systems or resources, as it can lead to unintended consequences if not implemented correctly. Always test your code thoroughly and consider edge cases to ensure that your loops are functioning as intended and do not cause any issues.
"""
import random

print("=============================== Loops in Python =============================== ")
# print("\n")

# print("=============================== While Loops in Python =============================== ")
# print("\n")
# # simple while loop
# x = 1

# while x < 10:
#     print(f'Iteration {x}')
#     x += 1

# Simple loan payment calculator using while loop
total_debt = 10000
payment = 133
# payment = int(input("Enter your monthly payment: "))
interest_rate = 0.10
months = 0

# while total_debt > 0:
#     print(f'Owed: ${total_debt:.2f}')
#     # Without interest rate
#     total_debt = total_debt - payment
#     # With interest rate
#     # total_debt = total_debt * (1 + interest_rate) - payment
#     months += 1

# years = months / 12
# print(f'Loan paid off in {months} months.')
# print("\n")
# print(f'Loan paid off in {years:.1f} years.')
# print("\n")

print("=============================== For Loops in Python =============================== ")
# Simple integer addition using for loop
sum = 0

for num in range(0, 101):
    sum += num
print(f'The sum of the first 100 integers is: {sum}')
print("\n")

# Print names from list of employees
employees = ['Chloe', 'Jack', 'Sophie', 'Liam', 'Tom']
for employee in employees:
    print(employee)
print("\n")

attendees = [
    ['Chloe', 'girl', 'large'],
    ['Jack', 'boy', 'medium'],
    ['Sophie', 'girl', 'small'],
    ['Liam', 'boy', 'large'],
    ['Tom', 'boy', 'medium']
]

for attendee in attendees:
    print(f'Name: {attendee[0]}, Gender: {attendee[1]}, Size: {attendee[2]}')
print("\n")

# Using if statements in for loops
for attendee in attendees:
    if 'small' in attendee and 'girl' in attendee:
        print(attendee)
       
    if 'girl' in attendee:
        print(attendee[0])
        print(f'{attendee[0]} is a girl.')
    else:
        print(attendee[0])
        print(f'{attendee[0]} is a boy.')   
