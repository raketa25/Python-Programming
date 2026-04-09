import random
from NumberGuess_art import logo


# function to set the game difficulty
HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10

def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Function to chek the users guess against the actual answer and return feedback

def check_guess(guess, answer, turns):
    """Checks the user's guess against the actual answer and returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! Congratulations!\n. The answer was {answer}.")

    return guess, turns   # Return the guess and turns to indicate a correct answer

# Function to start the game.
def play_game():
    print(logo)
    print("welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")  # For testing purposes, this line can be removed in production.
    print("\n")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Letting the player submit a guess and checking it against the answer
        guess = int(input("Make a guess: "))
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you loose.")
            return  # Exit the game if the player has no more turns
        elif guess != answer:
            print("Guess again.")

# Let's start the game
play_game()
