"""
CMPSC 132 - Practice Final Project
Number Guessing Game

Description:
A terminal-based number guessing game where the computer randomly chooses
a number and the player tries to guess it.

Features:
- Difficulty levels
- Input validation
- Attempt tracking
- High/low feedback
- Replay option
"""

import random

# Constants
EASY_RANGE = 10
MEDIUM_RANGE = 50
HARD_RANGE = 100


def display_welcome():
    """Displays the welcome message."""
    print("Welcome to the Number Guessing Game!")
    print("I will generate a random number, and you will try to guess it.")
    print()


def choose_difficulty():
    """Asks the user to choose a difficulty and returns the max value."""
    print("Choose a difficulty level:")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return EASY_RANGE
        if choice == "2":
            return MEDIUM_RANGE
        if choice == "3":
            return HARD_RANGE

        print("Invalid choice. Please enter 1, 2, or 3.")


def get_valid_guess(max_number):
    """Prompts the user for a valid integer guess in range."""
    while True:
        user_input = input(f"Enter your guess (1 to {max_number}): ").strip()

        try:
            guess = int(user_input)
            if 1 <= guess <= max_number:
                return guess
            print(f"Guess must be between 1 and {max_number}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def play_round():
    """Plays one round of the game."""
    max_number = choose_difficulty()
    secret_number = random.randint(1, max_number)
    attempts = 0

    print()
    print(f"I have chosen a number between 1 and {max_number}.")
    print("Try to guess it!")

    while True:
        guess = get_valid_guess(max_number)
        attempts += 1

        if guess < secret_number:
            print("Too low! Guess a higher number.")
        elif guess > secret_number:
            print("Too high! Guess a lower number.")
        else:
            print()
            print("Congratulations! You guessed the number!")
            print(f"The secret number was {secret_number}.")
            print(f"It took you {attempts} attempt(s).")
            break

def play_again():
    """Asks the user if they want to play again."""
    while True:
        answer = input("Would you like to play again? (yes/no): ").strip().lower()

        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False

        print("Please enter yes or no.")


def main():
    """Main function that runs the game."""
    display_welcome()

    while True:
        play_round()
        print()

        if not play_again():
            print("Thanks for playing!")
            break

        print()


if __name__ == "__main__":
    main()