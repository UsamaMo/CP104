"""
-------------------------------------------------------
[Assignment 3, Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-18"
-------------------------------------------------------
"""

# import
from functions import multiply_fractions

# input
num1 = int(input("Numerator 1: "))
denom1 = int(input("Denominator 1: "))
num2 = int(input("Numerator 2: "))
denom2 = int(input("Denominator 2: "))

# function
num_total, denom_total, product = multiply_fractions(
    num1, denom1, num2, denom2)

# output
print()
print(f"Result: {num_total}/{denom_total} = {product}")
