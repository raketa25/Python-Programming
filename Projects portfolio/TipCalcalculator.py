"""
This is a simple tip calculator that takes the total bill, the percentage of tip, and the number of people to split the bill. It then calculates how much each person should pay including the tip.
"""

print("Welcome to the the tip calculator\n")
print("========================= Let's Go! ==========================")
print('\n')
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_for_each = round(bill*(1 + tip/100)/people, 3)
print("======================= bill per person ======================\n")
print(f"Each person should pay: ${bill_for_each:.2f}")