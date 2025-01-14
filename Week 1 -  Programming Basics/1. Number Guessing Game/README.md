# Number Guessing Game

A simple interactive command-line game where players try to guess a randomly selected number within a custom range.

## Features

- Custom range selection: Players can set their own minimum and maximum numbers
- Interactive feedback: "Too high" or "Too low" hints after each guess
- Guess counter: Tracks the number of attempts needed to find the number
- Input validation: Handles invalid inputs gracefully
- Play again option: Multiple rounds can be played in one session

## Requirements

- Python 3.x
- No additional packages required (uses only Python standard library)

## How to Play

1. Run the game:
   ```bash
   python number_guessing_game.py
   ```

2. Follow the prompts to:
   - Enter the minimum number for your range
   - Enter the maximum number for your range
   - Start guessing numbers

3. After each guess, you'll receive feedback:
   - "Too high!" if your guess is above the target
   - "Too low!" if your guess is below the target
   - The game will ensure your guesses stay within the chosen range

4. When you guess correctly, you'll see:
   - A congratulations message
   - The number of guesses it took
   - An option to play again

## Tips

- Choose a reasonable range for more enjoyable gameplay
- Use the "Too high" and "Too low" hints to narrow down your guesses
- Try to guess the number in as few attempts as possible 