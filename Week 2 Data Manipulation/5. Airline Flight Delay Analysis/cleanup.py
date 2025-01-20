import os
import shutil

def cleanup_project():
    # Files to keep
    essential_files = {
        'flight_analysis.py',
        'README.md',
        'requirements.txt',
        '2015_flights.csv',
        'airports.csv'
    }
    
    # Remove __pycache__ directories
    if os.path.exists('__pycache__'):
        shutil.rmtree('__pycache__')
    
    # Remove non-essential files
    for file in os.listdir('.'):
        if os.path.isfile(file) and file not in essential_files:
            if file.endswith('.csv') or file.endswith('.py'):
                print(f"Removing: {file}")
                os.remove(file)

if __name__ == "__main__":
    cleanup_project() 