# https://github.com/adamtanguf/lab10-AT-AT/edit/main/test_calculator.py
# Partner 1: Adam Tang
# Partner 2: Adam Tang (solo)
git clone 
cd <repository_folder>
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
def logarithm(base, num):
    if base <= 0 or base == 1 or num <= 0:
        raise ValueError("Invalid base or number for logarithm")
    return math.log(num, base)

def exponent(base, power):
    return base ** power


