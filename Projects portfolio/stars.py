print("Welcome to the automatic stars printing challenge\n")

# first method with for loop
def print_stars_for(n):
    for i in range(n):
        print("*" * (i + 1))

# Second method with while loop
def print_stars_while(n):
    i = 0
    while i < n + 1:
        print("*" * i)
        i += 1

# Test of the function with a given number of stars
print_stars_for(5)
print("\n")
print_stars_while(5)
