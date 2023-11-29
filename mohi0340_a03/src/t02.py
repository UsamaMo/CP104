"""
-------------------------------------------------------
[Assignment 3, Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-18"
-------------------------------------------------------
"""
# import
from functions import mow_lawn

# input
width = float(input("Width (m):"))
length = float(input("Length (m):"))
speed = float(input("Speed (m^2/minute):"))

# function
time = mow_lawn(width, length, speed)

# output
print()
print(f"Mowing the lawn takes {time:.0f} minutes")
