"""
-------------------------------------------------------
[Lab 4, Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-08"
-------------------------------------------------------
"""

# Import
from functions import square_pyramid

# Inputs
base = float(input("Length of base:"))
height = float(input("Perpendicular height of pyramid:"))

# function
sh, area, vol = square_pyramid(base, height)

# Output
print("")
print(f"Slant height of square pyramid: {sh:.2f} ")
print(f"Area of square pyramid: {area: .2f}")
print(f"Volume of square pyramid: {vol:.2f}")
