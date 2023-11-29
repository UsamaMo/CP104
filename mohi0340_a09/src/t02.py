"""
-------------------------------------------------------
[Assignment 9 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-12-05"
-------------------------------------------------------
"""
# import
from functions import file_integers

# input
fh = open('numbers.txt', 'r', encoding='utf-8')

# function
numbers = file_integers(fh)

# output
print(f'{numbers}')
