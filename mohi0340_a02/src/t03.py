"""
-------------------------------------------------------
[Assignment 2, Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-29"
-------------------------------------------------------
"""

# inputs
wrongdate = int(input("Enter a date in the format MMDDYYYY: "))

# formulas
day = (wrongdate % 1000000) // 10000
month = wrongdate // 1000000
year = wrongdate % 10000

# outputs
print(f"The reformatted date: {year}/{month:02d}/{day:02d}")
