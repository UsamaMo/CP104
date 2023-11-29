"""
-------------------------------------------------------
[Assignment 5, Task 5]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-15"
-------------------------------------------------------
"""

# Imports
from functions import sum_factors

# input
num = int(input("Enter number: "))

# function
total = sum_factors(num)

# output
print()
print(f"sum_factors({num}) -> {total}")
