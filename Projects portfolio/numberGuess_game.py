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