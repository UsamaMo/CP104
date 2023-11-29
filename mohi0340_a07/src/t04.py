"""
-------------------------------------------------------
[Assignment 7, Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-22"
-------------------------------------------------------
"""

# imports
from functions import subtract_lists
from functions import list_positives

# outputs
print("Minuend After: ")
minuend = list_positives()

print("Remove Subtrahend: ")
subtrahend = list_positives()

print(f"subtract_lists[({minuend}, {subtrahend})] -> None")

# function
subtract_lists(minuend, subtrahend)

print(f"{minuend}")
