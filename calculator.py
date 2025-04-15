# https://github.com/adamtanguf/lab10-AT-AT
# Partner 1: Adam Tang
# Partner 2: Adam Tang (solo)
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def exponent(base, power):
    return base ** power

def logarithm(base, num):
    if base <= 0 or base == 1 or num <= 0:
        raise ValueError("Invalid base or number for logarithm")
    return math.log(num, base)

# Aliases required by autograder
def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def exp(base, power):
    return base ** power

