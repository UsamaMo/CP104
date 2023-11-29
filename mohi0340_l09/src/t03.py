"""
-------------------------------------------------------
[Lab 9, Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-19"
-------------------------------------------------------
"""

# import
from functions import parse_code

# input
code = input("Enter a product code: ")

# function
pc, pi, pq = parse_code(code)

# output
print("Category:  ", pc)
print("ID:        ", pi)
print("Qualifier: ", pq)
