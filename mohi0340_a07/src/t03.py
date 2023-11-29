"""
-------------------------------------------------------
[Assignment 7, Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-22"
-------------------------------------------------------
"""

# import
from functions import list_indexes

# input
values = [5, 1, 8, 9, 5, 2, 5, 3]
target = int(input("Enter value to look for: "))

# function
indexes = list_indexes(values, target)

# output
print(indexes)
