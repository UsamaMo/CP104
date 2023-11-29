"""
-------------------------------------------------------
[Lab 5, Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-22"
-------------------------------------------------------
"""
# import
from functions import closest

# input
target = float(input("Enter Target: "))
v1 = float(input("Enter v1: "))
v2 = float(input("Enter v2: "))

# function
result = closest(target, v1, v2)


# output
print(f"Closest value to {target} is {result}")
