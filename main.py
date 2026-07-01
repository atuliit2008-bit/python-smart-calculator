"""
main.py
Professional Smart Calculator
"""

from calculator import *


def show_menu():
    print("\n" + "=" * 40)
    print("        SMART CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulus")
    print("8. Floor Division")
    print("9. Exit")
    print("=" * 40)


while True:

    show_menu()

    choice = input("Enter your choice (1-9): ")

    if choice == "9":
        print("\nThank you for using Smart Calculator.")
        break

    try:

        if choice == "6":

            number = float(input("Enter number: "))
            result = square_root(number)
            print("Result =", result)
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)

        elif choice == "2":
            result = subtract(a, b)

        elif choice == "3":
            result = multiply(a, b)

        elif choice == "4":
            result = divide(a, b)

        elif choice == "5":
            result = power(a, b)

        elif choice == "7":
            result = modulus(a, b)

        elif choice == "8":
            result = floor_division(a, b)

        else:
            print("Invalid Choice!")
            continue

        print("Result =", result)

    except ValueError:
        print("\nPlease enter valid numbers.")