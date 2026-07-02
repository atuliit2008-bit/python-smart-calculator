from calculator import *

print("=" * 40)
print("      SMART CALCULATOR")
print("=" * 40)

while True:

    try:

        print("\nChoose Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Modulus")
        print("8. Floor Division")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == "9":
            print("\nThank you for using Smart Calculator!")
            break

        if choice == "6":
            number = float(input("Enter number: "))
            print("Answer =", square_root(number))
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Answer =", add(num1, num2))

        elif choice == "2":
            print("Answer =", subtract(num1, num2))

        elif choice == "3":
            print("Answer =", multiply(num1, num2))

        elif choice == "4":
            print("Answer =", divide(num1, num2))

        elif choice == "5":
            print("Answer =", power(num1, num2))

        elif choice == "7":
            print("Answer =", modulus(num1, num2))

        elif choice == "8":
            print("Answer =", floor_division(num1, num2))

        else:
            print("Invalid Choice!")

    except ValueError as error:
        print("\nInput Error:", error)

    except ZeroDivisionError as error:
        print("\nMath Error:", error)

    except Exception as error:
        print("\nUnexpected Error:", error)