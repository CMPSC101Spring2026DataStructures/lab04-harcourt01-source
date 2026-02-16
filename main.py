
# Basic Rock Paper Scissors Game
# Name: Alexander Harcourt
# Date: Feb. 15, 2026

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

# Implement this function to get and validate the user's choice.
def get_user_choice():
	"""Prompts the user for their choice and returns 'rock', 'paper', or 'scissors'."""
	while True: 
		user_input = console.input(f"Choose rock (1), paper (2), or scissors (3): ").strip().lower()
		
		if user_input == "1" or user_input == "rock":
			user_choice = "rock"
			return user_choice
		if user_input == "2" or user_input == "paper":
			user_choice = "paper"
			return user_choice
		if user_input == "3" or user_input == "scissors": # Each is a verification
			user_choice = "scissors"
			return user_choice
		else:
			console.print("Incorrect Input. Try Again.")

# Implement this function to randomly select the computer's choice.
def get_computer_choice():
	"""Randomly returns 'rock', 'paper', or 'scissors' for the computers input."""
	computer_choice = random.choice(choices)
	console.print(f"Computer Chose: {computer_choice}")
	return computer_choice

# Implement this function to determine the winner of a round.
def determine_winner(user_choice, computer_choice, user_score, computer_score):
	"""Returns 'user', 'computer', or 'tie' based on the choices. Also returns the round winner. """
	if user_choice == computer_choice:
		console.print("It Was A Tie!")
		winner = "Both"
	elif ((user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper')):
		console.print("User Won This Round!")
		winner = "USER"
	else:
		console.print("Computer Won This Round!")
		winner = "COM"
	return winner


# Implement this function to print the round result with color.
def print_round_result(user_score, computer_score):
	"""Prints the scores and the winner of the game."""
	console.print("[bold underline]Game Finished!")
	console.print(f"[blue]Your Score: {user_score}")
	console.print(f"[green]Computer Score: {computer_score}")

	if user_score > computer_score:
		console.print("[bold]You Won the Game!!!")
	if user_score < computer_score:
		console.print("[bold]Computer won the game.")
	else:
		console.print("[bold]Its a Tie!")
		

# Implement the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		user_choice = get_user_choice()
		computer_choice = get_computer_choice()

		winner = determine_winner(user_choice, computer_choice, user_score, computer_score) # Updates scores locally
		if winner == "COM":
			computer_score += 1
		if winner == "USER":
			user_score += 1
		if winner == "Both":
			x = "y"   # Just using this to make sure there is no error when it is a tie

	console.print()
	print_round_result(user_score, computer_score)

if __name__ == "__main__":
	main()