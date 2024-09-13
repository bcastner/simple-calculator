import math


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
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


# Function for exponentiation
def power(x, y):
    return x ** y


# Function to find the square root of a number
def square_root(x):
    if x < 0:
        return "You cannot take the square root of a negative number!"
    else:
        return math.sqrt(x)


# Function to find the remainder (modulus)
def modulus(x, y):
    return x % y


# Function to calculate the factorial of a number
def factorial(x):
    if x < 0:
        return "Error, the factorial of a negative number does not exist."
    elif x == 0 or x == 1:
        return 1
    else:
        return math.factorial(x)


# Function to calculate percentage
def percentage(x, y):
    return (x / y) * 100


# Function to calculate logarithm
def logarithm(x, base):
    return math.log(x, base)


# Trigonometric functions (sine, cosine, tangent)
def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


# Inverse trigonometric functions (arcsine, arccosine, arctangent)
def arcsine(x):
    if -1 <= x <= 1:
        return math.degrees(math.asin(x))
    else:
        return "Error! Input out of range for arcsine."


def arccosine(x):
    if -1 <= x <= 1:
        return math.degrees(math.acos(x))
    else:
        return "Error! Input out of range for arccosine."


def arctangent(x):
    return math.degrees(math.atan(x))


# Convert between degrees and radians
def degrees_to_radians(x):
    return math.radians(x)


def radians_to_degrees(x):
    return math.degrees(x)


# Prime number checker
def is_prime(num):
    if num <= 1:
        return "Not a prime number."
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return "Not a prime number."
    return "It's a prime number."


# create the function for the calculator
def calculator():
    while True:
        print("\nBasic Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation (x^y)")
        print("6. Square Root")
        print("7. Modulus")
        print("8. Factorial")
        print("9. Percentage")
        print("10. Logarithm (log base x)")
        print("11. Sine")
        print("12. Cosine")
        print("13. Tangent")
        print("14. Arcsine")
        print("15. Arccosine")
        print("16. Arctangent")
        print("17. Degrees to Radians")
        print("18. Radians to Degrees")
        print("19. Prime Number Checker")
        print("20. Exit")

        # take input from the user
        choice = input("Enter the operation you would like to perform: ")

        if choice == '20':
            print("Exiting...")
            break
        if choice in ['1', '2', '3', '4', '5', '7', '9', '10']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '7':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '9':
                print(f"{num1} is {percentage(num1, num2)}% of {num2}")
            elif choice == '10':
                base = float(input("Enter the base for the logarithm: "))
                print(f"log({num1}, base {base}) = {logarithm(num1, base)}")

        elif choice == '6':
            try:
                num1 = float(input("Enter the number for the square root: "))
                print(f"sqrt of {num1} = {square_root(num1)}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == '8':
            try:
                num1 = int(input("Enter an integer for factorial: "))
                print(f"{num1}! = {factorial(num1)}")
            except ValueError:
                print("Invalid input, please enter a valid integer.")
        elif choice == '11':
            num1 = float(input("Enter the angle in degrees: "))
            print(f"sin({num1}) = {sine(num1)}")

        elif choice == '12':
            num1 = float(input("Enter the angle in degrees: "))
            print(f"cos({num1}) = {cosine(num1)}")

        elif choice == '13':
            num1 = float(input("Enter the angle in degrees: "))
            print(f"tan({num1}) = {tangent(num1)}")

        elif choice == '14':
            num1 = float(input("Enter a value between -1 and 1 for arcsine: "))
            print(f"arcsin({num1}) = {arcsine(num1)}")

        elif choice == '15':
            num1 = float(input("Enter a value between -1 and 1 for arccosine: "))
            print(f"arccos({num1}) = {arccosine(num1)}")

        elif choice == '16':
            num1 = float(input("Enter a value for arctangent: "))
            print(f"arctan({num1}) = {arctangent(num1)}")

        elif choice == '17':
            num1 = float(input("Enter the angle in degrees to convert to radians: "))
            print(f"{num1} degrees = {degrees_to_radians(num1)} radians")

        elif choice == '18':
            num1 = float(input("Enter the angle in radians to convert to degrees: "))
            print(f"{num1} radians = {radians_to_degrees(num1)} degrees")

        elif choice == '19':
            num1 = int(input("Enter an integer to check if it’s prime: "))
            print(is_prime(num1))
        else:
            print("Invalid choice! Please select a valid operation.")


# run the calculator
calculator()
