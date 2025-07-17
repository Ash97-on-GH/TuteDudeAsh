'''
Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
'''
from math import *
n = float(input("Enter a number: "))
print("Square root: ",sqrt(n))
print("logarithm: ",log(n))
print("sine: ",sin(n))