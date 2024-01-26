#!/usr/bin/env python3

import random

def get_user_choice():
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 0  # It's a tie
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return 1  # User wins
    else:
        return -1  # Computer wins

def play_game():
    print("Let's play Rock, Paper, Scissors!")

    rounds = int(input("Enter the number of rounds: "))
    user_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score - You: {user_score} | Computer: {computer_score}")

    print("\nGame Over!")

    if user_score > computer_score:
        print("Congratulations! You win the game!")
    elif user_score < computer_score:
        print("Oops! Computer wins the game.")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    play_game()
