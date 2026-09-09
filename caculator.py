# Simple Calculator Program for Beginners

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    # Check if dividing by zero
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Main calculator function
def calculator():
    # Display welcome message
    print("Welcome to the Simple Calculator!")
    
    # Loop to keep the calculator running
    while True:
        # Get the first number from the user
        try:
            num1 = float(input("\nEnter the first number: "))
        except ValueError:
            # Handle invalid input (if user enters text instead of number)
            print("Invalid input! Please enter a valid number.")
            continue
        
        # Get the operator from the user
        operator = input("Choose an operator (+, -, *, /): ")
        
        # Get the second number from the user
        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            # Handle invalid input
            print("Invalid input! Please enter a valid number.")
            continue
        
        # Choose the correct operation based on the operator
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            # Handle invalid operator
            print("Invalid operator! Please choose +, -, *, or /")
            continue
        
        # Display the result
        print(f"\n{num1} {operator} {num2} = {result}")
        
        # Ask the user if they want to perform another calculation
        another = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        
        # Check if the user wants to continue or quit
        if another != 'yes' and another != 'y':
            print("Thank you for using the Simple Calculator. Goodbye!")
            break

# Start the calculator program
calculator()
