import art
from random import randint

# defining function if guessed number is lower than secret number
def num_lower():
        print("Too low.")
        print("Guess again.")


# defining function if guessed number is bigger than secret number
def num_bigger():
        print("Too high.")
        print("Guess again.")


# if player's guess == to secret number
def right_guess():
        print(f"You got it. The secret number was {secret_num}.")


# if it is last guess and player didn't guess the secret number
def last_guess():
    print(f"You've run out of guesses. The secret number was {secret_num}.")


# defining easy mode
def easy_mode():
    attempts = 10
    while attempts != 0:
        # remaining attempts
        print(f"You have {attempts} remaining attempts to guess.")
        # player's guess
        guess = int(input("Make a guess: "))
        # I needed to put this before last guess otherwise it would trigger last guess even though I would guess the secret number
        if guess == secret_num:
            right_guess()
            break
        # last guess
        if attempts == 1:
            last_guess()
            break
        # assure that player entered valid number (from 1 to 100)
        if guess > 100:
            print("Please enter a number from 1 to 100.")
            attempts += 1
        elif guess < secret_num:
            num_lower()
        elif guess > secret_num:
            num_bigger()
        # subtract 1 attempt
        attempts -= 1


def hard_mode():
    attempts = 5
    while attempts != 0:
        # remaining attempts
        print(f"You have {attempts} remaining attempts to guess.")
        # player's guess
        guess = int(input("Make a guess: "))
        # I needed to put this before last guess otherwise it would trigger last guess even though I would guess the secret number
        if guess == secret_num:
            right_guess()
            break
        # last guess
        if attempts == 1:
            last_guess()
            break
        # assure that player entered valid number (from 1 to 100)
        if guess > 100:
            print("Please enter a number from 1 to 100.")
            attempts += 1
        elif guess < secret_num:
            num_lower()
        elif guess > secret_num:
            num_bigger()
        # subtract 1 attempt
        attempts -= 1


playing = True
while playing:
    # asking player if he wants to play
    play = input("Do you want to play my number guessing game? Type 'yes' or 'no': ").lower()
    if play == "yes":
        # random number
        secret_num = randint(1,100)
        # printing ASCII ART
        print(art.logo)

        # welcoming the player
        print("Welcome to my number guessing game!")
        # guess number from 1 to 100
        print("I'm thinking of a number from 1 to 100.")

        # easy or hard mode
        mode = input("Choose difficulty: Type 'easy' or 'hard': ").lower()

        # easy mode
        if mode == "easy":
            easy_mode()
        elif mode == "hard":
            hard_mode()
    else:
        print("Thank you for playing. See you next time :)")
        playing = False





