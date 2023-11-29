"""
-------------------------------------------------------
[Assignment 3, Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-18"
-------------------------------------------------------
"""

# import
from functions import date_extract

# input
date_number = int(input("Enter a date in the format MMDDYYYY:"))

# function
year, month, day = date_extract(date_number)

# output
print()
print(f"The reformatted date: {year}/{month:02}/{day:02}")
