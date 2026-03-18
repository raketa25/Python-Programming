import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomized

password_easy = []

# Adding letters, symbols and numbers

for _ in range(1, nr_letters + 1):
    password_easy.append(random.choice(letters))

for _ in range(0, nr_symbols):
    password_easy.append(random.choice(symbols))

for _ in range(1, nr_numbers + 1):
    password_easy.append(random.choice(numbers))

# Joining to create the easy password

easy_password = ''.join(password_easy)
print(f"The easy password is: {easy_password}")

# Hard Level
# Shuffle the list to randomize the order
random.shuffle(password_easy)

# Join to create the hard password
# hard_password = ''.join(password_easy)

hard_password = ""
for char in password_easy:
    hard_password += char

print(f"The hard password (randomized order) is: {hard_password}")