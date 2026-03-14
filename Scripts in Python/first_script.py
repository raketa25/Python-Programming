import random
# =============================== Variables and Concatenation in Python =============================== #
# print("=============================== Variables and Concatenation in Python =============================== ")
# print("\n")
# print("================== Variables and Data Types in Python ================== ")
# print("\n")

# message = 'Hello'

# number_var = 7
# float_var = 7.0
# bool_var = True

# print(type(message))
# print(type(number_var))
# print(type(float_var))
# print(type(bool_var))

# Converting data types
# float_var = int(float_var)
# print(float_var)

# print("\n")
# print("================== Concatenation in Python ================== ")
# print("\n")
# first_name = "Chloe"
# last_name = "Obrian"
# age = 34

# Concatenating methods
# print((message) + (first_name) + (" ") + (last_name) + 'Im happy you are here')
# print((message),(first_name) + (" ") + (last_name) + 'Im happy you are here')
# print(f'{message} {first_name} {last_name} Im happy you are here')

# print(f"{message} {first_name} {last_name} I'm happy you're here")
# print(f'{message} {first_name} {last_name} I\'m happy you\'re here')

# print("\n")
# age = str(age)
# print((message) + (" ") + (first_name) + (" ") + (last_name) + ' you are ' + (age) + ' years old')
# # print(f"{message} {first_name} {last_name} you are {age} years old")
# print("\n")

# print("\n")
print("=============================== If Else Statements and Conditions in Python =============================== ")
# print("\n")

# var_num = 500
# var_num = int(input("Enter a number: "))
# var_num = random.randint(0, 150)
# print(f'Your number is: {var_num}')
# if var_num > 100:
#     print('That\'s a BIG NUMBER!')
# else:
#     print('That\'s a small number.')

# elif statment:
# if var_num > 50 and var_num <= 100:
#     print('Not BIG, or small!')
# elif var_num > 100:
#     print('That\'s a BIG NUMBER!')
# else:   
#     print('That\'s a small number.')

# if var_num < 50 or var_num > 100:
#     print('The number is on the edge!')
# else:
#     print('The number is in the middle!')


# Dealing with strings in if statements
var_string = 'Chloe'

message = 'Hello ' + var_string + ', welcome to the world of Python!'

if var_string in message:
    print(message)
else:
    print('The message is not for you.')

if var_string not in message:
    print('Try again later.')
else:
    print('I hope you liked your message!')

