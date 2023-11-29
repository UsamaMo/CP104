"""
-------------------------------------------------------
[Assignment 9 Task 6]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-12-06"
-------------------------------------------------------
"""
# import
from functions import get_addresses

# input
fh = open('addresses.txt', 'r', encoding='utf-8')

# function
addresses = get_addresses(fh)

# output
for i in addresses:
    print(i)
