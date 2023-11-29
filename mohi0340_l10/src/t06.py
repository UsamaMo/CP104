"""
-------------------------------------------------------
[Lab 10, Task 6]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""
# import
from functions import number_stats

# file location
file_1 = "numbers.txt"

# file
fh = open(file_1)

# function
smallest, largest, total, average = number_stats(fh)

# output
print(f"""Smallest: {smallest}
Largest: {largest}
Total: {total:.2f}
Average: {average:.2f}""")
