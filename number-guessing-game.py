# Number Guessing Game
# Author: Muhammad Ameen J.
# Description: A fun interactive game where the player guesses a random number

import random

def get_difficulty():
    print("\nSelect Difficulty:")
    print("  1. Easy   (1-50,  10 attempts)")
    print("  2. Medium (1-100,  7 attempts)")
    print("  3. Hard   (1-200,  5 attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == "1":
            return 50, 10, "Easy"
        elif choice == "2":
            return 100, 7, "Medium"
        elif choice == "3":
            return 200, 5, "Hard"
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

def play_game():
    print("=" * 45)
    print("        NUMBER GUESSING GAME")
    print("=" * 45)

    max_number, max_attempts, difficulty = get_difficulty()
    secret = random.randint(1, max_number)
    attempts = 0

    print(f"\n[{difficulty} Mode] Guess a number between 1 and {max_number}")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} — Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess == secret:
            print("\n" + "=" * 45)
            print(f"  CORRECT! The number was {secret}!")
            print(f"  You guessed it in {attempts} attempt(s)!")
            if attempts == 1:
                print("  WOW! First try! Genius level!")
            elif attempts <= max_attempts // 2:
                print("  Excellent! Very few attempts!")
            else:
                print("  Good job! You got it!")
            print("=" * 45)
            return

        elif guess < secret:
            print(f"  Too LOW! Try a higher number. ({remaining-1} attempts left)")
        else:
            print(f"  Too HIGH! Try a lower number. ({remaining-1} attempts left)")

        if remaining - 1 == 1:
            print("  WARNING: Last attempt!")

    print("\n" + "=" * 45)
    print(f"  GAME OVER! The number was {secret}.")
    print("  Better luck next time!")
    print("=" * 45)

def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
