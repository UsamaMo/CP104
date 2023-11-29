"""
-------------------------------------------------------
[Assignment 9 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-12-05"
-------------------------------------------------------
"""

# import
from functions import file_stats

# input
fh = open("addresses.txt", "r", encoding="utf-8")

# function
ucount, lcount, dcount, wcount = file_stats(fh)

# output
print(f"({ucount},{lcount},{dcount},{wcount})")
