import random

rock = ""
paper = ""
scissors = ""
game_images = [rock, paper, scissors]
# Items = ["Rock", "Paper", "Scissors"]
# num_item = len(Items)
# random_choice = random.randint(0, num_item -1)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors \n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

# computer_choice = Items[random_choice]
computer_choice = random.randint(0, 2)
print(f"computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("you lose!")
