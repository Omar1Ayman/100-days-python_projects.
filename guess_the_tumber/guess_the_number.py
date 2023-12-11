logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
import random
def type_level(type_game):
    if type_game == "easy":
        level = EASY_LEVEL_TURNS
    elif type_game == "hard":
        level = HARD_LEVEL_TURNS
    else:
        return "invalid input"
    guess_number = random.randint(1,100)
    game_is_over = False
    counter = 1
    while counter <= level:
        if counter == level:
            user_guess = int(input(f"You have {1+level-counter} attempts remaining to guess the number this is a last attempt. \n Make a guess: "))
            if user_guess == "":
                return "you have to type somthing"
        else:
            user_guess = int(input(f"You have {1+level-counter} attempts remaining to guess the number. \n Make a guess: "))
        if user_guess > 100 or user_guess < 1:
            counter = level
            return "invalid number not in range."
        elif user_guess < guess_number:
            counter +=1
            print("Too Low.")
        elif user_guess > guess_number:
            counter +=1
            print("Too Heigh")
        else:
            print(f"Yo win. {user_guess} = {guess_number}")
            counter = level
    else:
        print("finish!")




def Guess_Number():
    print(logo)
    print("Welcom to the Number Guessing Game!")
    print("I`m thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        type_level("easy")
    elif level == "hard":
        type_level("hard")
    else:
        print("finish!")
 


while input("do you want to guess again? 'yes' or 'no' ") == "yes":
        Guess_Number()
