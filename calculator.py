# """
# calculator.py
# Contains all mathematical functions used by the Smart Calculator.
# """

import math


def add(a, b):
    # """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    # """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    # """Return the product of two numbers."""
    return a * b


def divide(a, b):
    # """Return the division of two numbers."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def power(a, b):
    # """Return a raised to the power b."""
    return a ** b


def modulus(a, b):
    # """Return the remainder."""
    return a % b


def floor_division(a, b):
    # """Return floor division."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a // b


def square_root(a):
    # """Return square root."""
    if a < 0:
        return "Error! Negative number."
    return math.sqrt(a)