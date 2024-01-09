#!/usr/bin/env python3
def calculator():
    first_number = float(input("Enter your first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    second_number = float(input("Enter your second number: "))
    
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("ERROR: Cannot divide by zero.")
            return
    print("Result:", result)

calculator()