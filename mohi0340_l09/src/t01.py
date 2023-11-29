"""
-------------------------------------------------------
[Lab 9, Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-19"
-------------------------------------------------------
"""

# import
from functions import is_hydroxide

# input
chemical = input('Enter a chemical formula: ')

# function
hydroxide = is_hydroxide(chemical)

# output
if is_hydroxide(chemical):
    print('%s is a hydroxide.' % chemical)

else:
    print('%s is not a hydroxide.' % chemical)
