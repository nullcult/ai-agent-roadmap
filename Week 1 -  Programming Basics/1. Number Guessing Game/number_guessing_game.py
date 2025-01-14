import random

def play_game():
    print("\n=== Number Guessing Game ===")
    
    # Get the range from the user
    while True:
        try:
            min_num = int(input("Enter the minimum number for the range: "))
            max_num = int(input("Enter the maximum number for the range: "))
            if min_num >= max_num:
                print("Maximum number must be greater than minimum number. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter valid numbers.")
    
    # Generate random number within the specified range
    secret_number = random.randint(min_num, max_num)
    guesses = 0
    
    print(f"\nI'm thinking of a number between {min_num} and {max_num}.")
    
    while True:
        try:
            # Get user's guess
            guess = int(input("\nEnter your guess: "))
            guesses += 1
            
            # Check the guess
            if guess < min_num or guess > max_num:
                print(f"Please guess a number between {min_num} and {max_num}.")
            elif guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"\nCongratulations! You've guessed the number in {guesses} {'guess' if guesses == 1 else 'guesses'}!")
                break
                
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main() 