"""
-------------------------------------------------------
[Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""

# import
from functions import product_largest

# input
v1 = float(input("Enter a number: "))
v2 = float(input("Enter a number: "))
v3 = float(input("Enter a number: "))

# function
product = product_largest(v1, v2, v3)

# output
print(f"product_largest({v1:.0f},{v2:.0f},{v3:.0f})->{product:.0f} ")
