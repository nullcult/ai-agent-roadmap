import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice! Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    return "computer"

def play_game(best_of):
    user_score = 0
    computer_score = 0
    games_needed = (best_of // 2) + 1
    
    print(f"\nBest of {best_of} games mode!")
    
    while max(user_score, computer_score) < games_needed:
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            print("You win this round!")
            user_score += 1
        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
    
    print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    else:
        print("Game Over! Computer wins!")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        print("\nSelect game mode:")
        print("1. Best of 3")
        print("2. Best of 5")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            play_game(3)
        elif choice == "2":
            play_game(5)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 