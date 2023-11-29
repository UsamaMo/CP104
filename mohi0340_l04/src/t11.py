"""
-------------------------------------------------------
[Lab 4, Task 11]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-08"
-------------------------------------------------------
"""

# Import
from functions import slope

# Inputs
x1 = float(input("Enter first x:"))
y1 = float(input("Enter first y:"))
x2 = float(input("Enter second x:"))
y2 = float(input("Enter second y:"))

# function
slp = slope(x1, y1, x2, y2)

# Output
print("")
print(f"The slope is {slp:.1f}")
