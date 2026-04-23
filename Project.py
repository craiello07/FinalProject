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