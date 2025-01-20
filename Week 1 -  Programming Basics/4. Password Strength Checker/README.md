# Password Strength Checker

A Python program that evaluates password strength and provides improvement suggestions.

## Features

- Evaluates password strength based on multiple criteria:
  - Length (minimum 8 characters)
  - Presence of uppercase letters
  - Presence of lowercase letters
  - Presence of numbers
  - Presence of special characters
- Checks against common passwords
- Provides specific improvement suggestions
- Generates example improved passwords

## Installation

1. Make sure you have Python 3.6 or higher installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the program:
```bash
python password_checker.py
```

Follow the prompts to enter passwords for evaluation. Enter 'q' to quit the program.

## Scoring System

The password strength is evaluated on a scale of 0-5:
- Very Weak (0-1 points)
- Weak (2 points)
- Moderate (3 points)
- Strong (4 points)
- Very Strong (5+ points)

Points are awarded for:
- Password length (1 point per 8 characters)
- Including uppercase letters (1 point)
- Including lowercase letters (1 point)
- Including numbers (1 point)
- Including special characters (1 point)

Note: If a common password is detected, the score is automatically set to 0. 