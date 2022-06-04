# Calculator with system arguments
import sys

# Addition
def add(x, y):
    return x + y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y

# Subtraction
def subtract(x, y):
    return x - y

if __name__ == "__main__":
    # Check if the user entered two numbers
    if len(sys.argv) == 4:
        # Get the numbers from the system arguments
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])

        # Get the operator from the system arguments
        operator = str(sys.argv[2])

        # Check if the user entered a valid operator
        if operator == '+':
            print(add(num1, num2))
        elif operator == '-':
            print(subtract(num1, num2))
        elif operator == '*':
            print(multiply(num1, num2))
        elif operator == '/':
            print(divide(num1, num2))
        else:
            print("Invalid operator")
    else:
        print("Invalid numbers")
