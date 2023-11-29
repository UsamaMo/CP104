"""
-------------------------------------------------------
[Lab 11, Task 13]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-12-03"
-------------------------------------------------------
"""

# import
from functions import scalar_multiply

# input
matrix = [[-6, -6, -4, -5], [7, 3, 3, 8], [-6, 1, 6, 1]]


print(f"Matrix (without scalar multiplication: {matrix} ")
print()

# input
num = int(input("Enter number: "))


# function
scalar_multiply(matrix, num)

# output
print()
print(f'Matrix (with scalar multiplication: {matrix}')
