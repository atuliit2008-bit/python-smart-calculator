# """
# main.py
# Main program for Smart Calculator
# """

from calculator import *


def show_menu():
    # """Display calculator menu"""
    print("\n========== SMART CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulus")
    print("8. Floor Division")
    print("9. Exit")
    print("======================================")


while True:

    show_menu()

    choice = input("Enter your choice (1-9): ")

    if choice == "9":
        print("\nThank you for using Smart Calculator.")
        break

    if choice == "6":

        number = float(input("Enter number: "))

        print("Result =", square_root(number))

        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result =", add(a, b))

    elif choice == "2":
        print("Result =", subtract(a, b))

    elif choice == "3":
        print("Result =", multiply(a, b))

    elif choice == "4":
        print("Result =", divide(a, b))

    elif choice == "5":
        print("Result =", power(a, b))

    elif choice == "7":
        print("Result =", modulus(a, b))

    elif choice == "8":
        print("Result =", floor_division(a, b))

    else:
        print("Invalid choice!")