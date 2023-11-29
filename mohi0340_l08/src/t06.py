"""
-------------------------------------------------------
[Lab 8, Task 6]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
# import
from functions import list_stats

# constant
values = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]

# function
smallest, largest, total, average = list_stats(values)

# output
print(f"Values: {values}")
print()
print(f"Smallest value is: {smallest}")
print(f"Largest value is: {largest}")
print(f"Total value is: {total}")
print(f"Average value is: {average}")
