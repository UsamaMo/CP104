"""
-------------------------------------------------------
[Lab 8, Task 10]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
# import
from functions import min_search

# constants
a = [94, 96, -32, -19, -28, 96, -22, 71, 24, -32]

# function
indexes = min_search(a)

# output
print(f'Values: {a}')
print()
print(f'Indexes of minimums: {indexes}')
