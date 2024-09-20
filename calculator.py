# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division with validation for division by zero
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function for modulus
def modulus(x, y):
    return x % y

# Function for exponentiation
def exponentiate(x, y):
    return x ** y

# Display options to the user
def show_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")

# Main calculator function to take user input and call corresponding operation
def calculator():
    while True:
        show_menu()
        choice = input("Enter choice (1/2/3/4/5/6 or 'q' to quit): ")

        if choice == 'q':
            print("Exiting the calculator.")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            elif choice == '5':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")

            elif choice == '6':
                print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")

        else:
            print("Invalid Input! Please select a valid operation.")

# Run the calculator
calculator()
