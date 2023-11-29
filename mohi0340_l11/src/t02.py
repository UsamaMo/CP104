"""
-------------------------------------------------------
[Lab 11, Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-12-03"
-------------------------------------------------------
"""

# import
from functions import generate_matrix_char

# input
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

# function
matrix = generate_matrix_char(rows, cols)

# output
print()
print("Matrix of characters:")
print()
print(matrix)
