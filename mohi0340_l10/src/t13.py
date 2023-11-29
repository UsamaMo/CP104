"""
-------------------------------------------------------
[Lab 10, Task 13]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""

# imports
from functions import file_copy

# input
fh1 = input("Enter a file: ")
fh2 = input("Enter a file: ")

# open file
fh_1 = open(fh1, 'r')
fh_2 = open(fh2, 'w')

# function
file_copy(fh_1, fh_2)

# output
print(f'Copying {fh1} to {fh2}')
fh_1.close()
fh_2.close()
