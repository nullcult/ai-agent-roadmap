# Rock, Paper, Scissors Game

A simple command-line implementation of the classic Rock, Paper, Scissors game where you play against the computer.

## Features

- Single-player gameplay against computer
- Two game modes: Best of 3 or Best of 5
- Score tracking
- Input validation
- Random computer moves

## How to Play

1. Run the game:
   ```
   python rock_paper_scissors.py
   ```

2. Choose your game mode:
   - Best of 3
   - Best of 5
   - Quit

3. For each round:
   - Enter your choice (rock/paper/scissors)
   - The computer will randomly select its move
   - The winner of the round will be displayed
   - The score will be updated

4. The game continues until someone wins the majority of rounds
   - Best of 3: First to win 2 rounds
   - Best of 5: First to win 3 rounds

## Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both players choose the same option, it's a tie

## Requirements

- Python 3.x
- No additional packages required

## File Structure

- `rock_paper_scissors.py`: Main game file containing all the game logic
- `README.md`: Documentation file with game information and instructions

## Author

[Your Name]

## License

This project is open source and available under the MIT License. 