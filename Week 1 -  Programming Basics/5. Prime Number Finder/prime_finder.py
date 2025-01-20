def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sieve_of_eratosthenes(start, end):
    """Generate prime numbers using the Sieve of Eratosthenes algorithm."""
    # Create a boolean array "is_prime[0..end]" and initialize
    # all entries it as true
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(end ** 0.5) + 1):
        if sieve[i]:
            # Update all multiples of i starting from i*i
            for j in range(i * i, end + 1, i):
                sieve[j] = False

    # Create the list of prime numbers within the range
    return [i for i in range(max(2, start), end + 1) if sieve[i]]

def get_primes_in_range(start, end):
    """Generate a list of prime numbers within a given range."""
    # Use Sieve of Eratosthenes for ranges larger than 1000
    if end - start > 1000:
        return sieve_of_eratosthenes(start, end)
    return [num for num in range(max(2, start), end + 1) if is_prime(num)]

def visualize_primes(start, end):
    """Create a simple visualization of prime numbers in a range."""
    primes = get_primes_in_range(start, end)
    
    print(f"\nPrime numbers between {start} and {end}:")
    print("-" * 50)
    
    for number in range(start, end + 1):
        if number in primes:
            print("🟢", end=" ")  # Green circle for prime numbers
        else:
            print("⚪", end=" ")  # White circle for non-prime numbers
        if (number - start + 1) % 10 == 0:  # New line every 10 numbers
            print()
    print("\n")
    print(f"Found {len(primes)} prime numbers in this range.")

def main():
    while True:
        print("\nPrime Number Finder")
        print("1. Check if a number is prime")
        print("2. Find prime numbers in a range")
        print("3. Visualize prime numbers in a range")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            while True:
                try:
                    num = int(input("\nEnter a number to check (or 0 to go back): "))
                    if num == 0:
                        break
                    if is_prime(num):
                        print(f"{num} is a prime number!")
                    else:
                        print(f"{num} is not a prime number.")
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == '2':
            try:
                start = int(input("\nEnter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                if start > end:
                    start, end = end, start
                primes = get_primes_in_range(start, end)
                print(f"\nPrime numbers between {start} and {end}:")
                print(primes)
                print(f"\nFound {len(primes)} prime numbers in this range.")
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == '3':
            try:
                start = int(input("\nEnter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                if start > end:
                    start, end = end, start
                if end - start > 200:
                    print("\nWarning: Large ranges may be hard to visualize.")
                    if input("Continue? (y/n): ").lower() != 'y':
                        continue
                visualize_primes(start, end)
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == '4':
            print("\nThank you for using Prime Number Finder!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 