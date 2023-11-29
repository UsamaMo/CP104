"""
-------------------------------------------------------
[Lab 11, Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""

# import
from functions import generate_matrix_num

# inputs
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = float(input("Low value: "))
high = float(input("High value: "))
# value type either float or int
value_type = input("Type of values: ")

# function
matrix = generate_matrix_num(rows, cols, low, high, value_type)

# output
print()
print(matrix)
