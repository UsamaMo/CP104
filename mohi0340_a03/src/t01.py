"""
-------------------------------------------------------
[Assignment 3,Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-18"
-------------------------------------------------------
"""

# import
from functions import feet_to_acres

# input
square_footage = float(input("Square footage:"))

# function
acres = feet_to_acres(square_footage)

# output
print(f"{acres:.2f} is equivalent to {square_footage:,.2f} square feet")
