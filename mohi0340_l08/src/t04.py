"""
-------------------------------------------------------
[Lab 8, Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
# import
from functions import generate_integer_list

# input
n = int(input("Number of Values: "))
low = int(input("Low Value: "))
high = int(input("High Value: "))

# function
values = generate_integer_list(n, low, high)

# output
print()
print(f"{values}")
