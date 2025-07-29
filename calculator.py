# Simple Calculator using Python for PLP Assignment
# This script performs basic arithmetic operations: addition, subtraction, multiplication, and division.

# Get user input
num1 = input("First number: ")
num2 = input("Second number: ")
op = input("Choose operation (+, -, *, /): ")

# Convert numbers from string to float
num1 = float(num1)
num2 = float(num2)

# Doing the Math; Addition, subtraction, multiplication, and division respectively
if op == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Can't divide by zero.")
else:
    print("Unknown operation.")

# End of calculator.py