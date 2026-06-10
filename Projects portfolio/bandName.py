"""
This is a simple program that generates a band name based on the user's input. It asks the user for the name of the city they grew up in and the name of their pet, then combines those two pieces of information to create a potential band name. The program uses string concatenation to combine the city and pet names, and it displays the result to the user.
"""

print("="*50)
print("WELCOME TO THE BAND NAME GENERATOR!")
print("="*50)
city = input("What's the name of the city you grew up in?> ")
pet = input("What's the name of your pet?> ")

print(f"Your band name could be: {city} {pet}")