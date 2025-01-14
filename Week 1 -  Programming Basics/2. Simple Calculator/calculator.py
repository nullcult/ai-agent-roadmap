def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def format_number(num):
    return int(num) if num.is_integer() else num

def main():
    operations = {
        1: ("Addition", add),
        2: ("Subtraction", subtract),
        3: ("Multiplication", multiply),
        4: ("Division", divide)
    }
    
    while True:
        print("\n=== Simple Calculator ===")
        print("Select operation:")
        for key, (operation_name, _) in operations.items():
            print(f"{key}. {operation_name}")
        
        try:
            choice = int(input("Enter choice (1-4): "))
            if choice not in operations:
                print("Invalid choice! Please select 1-4")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            
            # Format the numbers for display
            num1_formatted = format_number(num1)
            num2_formatted = format_number(num2)
            result_formatted = format_number(result)
            
            print(f"\nResult: {num1_formatted} {operation_name} {num2_formatted} = {result_formatted}")
            
        except ValueError as e:
            if str(e) == "Cannot divide by zero!":
                print("\nError: Cannot divide by zero!")
            else:
                print("\nError: Please enter valid numbers!")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
        
        continue_calc = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if continue_calc != 'yes':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main() 