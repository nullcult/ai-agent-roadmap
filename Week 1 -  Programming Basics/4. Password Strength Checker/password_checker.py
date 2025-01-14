import re
import string
import json
from pathlib import Path

class PasswordStrengthChecker:
    def __init__(self):
        self.common_passwords = self._load_common_passwords()
        
    def _load_common_passwords(self):
        # In a real application, you might want to load this from a file
        return {
            '123456', 'password', 'qwerty', 'abc123', 'letmein',
            'admin', '123456789', '12345', 'welcome', 'password1'
        }
    
    def check_strength(self, password):
        score = 0
        feedback = []
        
        # Check length
        if len(password) < 8:
            feedback.append("Password is too short (minimum 8 characters)")
        else:
            score += len(password) // 8
            
        # Check for uppercase letters
        if not any(c.isupper() for c in password):
            feedback.append("Add uppercase letters")
        else:
            score += 1
            
        # Check for lowercase letters
        if not any(c.islower() for c in password):
            feedback.append("Add lowercase letters")
        else:
            score += 1
            
        # Check for numbers
        if not any(c.isdigit() for c in password):
            feedback.append("Add numbers")
        else:
            score += 1
            
        # Check for special characters
        special_chars = set(string.punctuation)
        if not any(c in special_chars for c in password):
            feedback.append("Add special characters (!@#$%^&*etc.)")
        else:
            score += 1
            
        # Check for common passwords
        if password.lower() in self.common_passwords:
            score = 0
            feedback.append("This is a commonly used password. Please choose a different one")
            
        # Calculate strength level
        strength = self._get_strength_level(score)
        
        return {
            'strength': strength,
            'score': score,
            'feedback': feedback
        }
    
    def _get_strength_level(self, score):
        if score <= 1:
            return "Very Weak"
        elif score == 2:
            return "Weak"
        elif score == 3:
            return "Moderate"
        elif score == 4:
            return "Strong"
        else:
            return "Very Strong"
    
    def suggest_improvements(self, password):
        result = self.check_strength(password)
        suggestions = result['feedback']
        
        if not suggestions:
            return ["Your password is already strong!"]
            
        improved = list(password)
        if "Add uppercase letters" in suggestions:
            if len(improved) > 0:
                improved[0] = improved[0].upper()
        if "Add numbers" in suggestions:
            improved.append('1')
        if "Add special characters" in suggestions:
            improved.append('!')
            
        if improved != list(password):
            suggestions.append(f"Example of improved password: {''.join(improved)}")
            
        return suggestions

def main():
    checker = PasswordStrengthChecker()
    
    while True:
        password = input("\nEnter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break
            
        result = checker.check_strength(password)
        print(f"\nPassword Strength: {result['strength']}")
        print(f"Score: {result['score']}/5")
        
        if result['feedback']:
            print("\nImprovement suggestions:")
            suggestions = checker.suggest_improvements(password)
            for suggestion in suggestions:
                print(f"- {suggestion}")
        else:
            print("\nGreat! Your password is strong.")
            
if __name__ == "__main__":
    main() 