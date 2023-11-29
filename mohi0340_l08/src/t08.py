"""
-------------------------------------------------------
[Lab 8, Task 8]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
# import
from functions import linear_search

# constant
a = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]


print(f"Values: {a}")

# input
v = int(input("Enter a integer from the list above: "))

# function
index = linear_search(a, v)

# output
print()
print(f"Index of {v}: {index}")
