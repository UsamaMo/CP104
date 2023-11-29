"""
-------------------------------------------------------
[Lab 5, Task 8]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-22"
-------------------------------------------------------
"""

# import
from functions import roman_numeral

# input
n = int(input("Enter a number from 1 to 10: "))

# function
numeral = roman_numeral(n)

# output
print(f"The Roman numeral equivalent of {n} is {numeral}")
