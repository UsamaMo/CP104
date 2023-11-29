"""
-------------------------------------------------------
[Assignment 7, Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-22"
-------------------------------------------------------
"""

# import
from functions import list_factors

# input
num = int(input("Enter Number to Factor: "))

# function
factors = list_factors(num)

# output
print()
print(f'list_factors({num})')
print(factors)
