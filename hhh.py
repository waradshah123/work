def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    # Greet the user and get their name
    name = input("Hello! What's your name? ")
    print(f"Welcome, {name}! Let's have some fun with numbers.")

    # Get three favorite numbers from the user
    numbers = []
    for i in range(1, 4):
        while True:
            try:
                num = int(input(f"Please enter your favorite number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("That's not a valid number! Please try again.")

    # Determine if the numbers are even or odd
    even_odd = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

    # Display even/odd information
    print("\nHere's what I found out about your numbers:")
    for num, parity in even_odd:
        print(f"The number {num} is {parity}.")

    # Calculate and display squares of the numbers
    print("\nNow, let's explore the squares of your favorite numbers:")
    for num in numbers:
        print(f"The square of {num} is {num ** 2}.")

    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    print(f"\nThe sum of your favorite numbers is: {total_sum}")

    # Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow! {total_sum} is a prime number. That's special!")
    else:
        print(f"{total_sum} is not a prime number, but it's still a great number!")

    # Closing message
    print(f"\nThanks for exploring numbers with me, {name}! I hope you had fun.")

if __name__ == "__main__":
    main()
