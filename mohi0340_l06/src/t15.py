"""
-------------------------------------------------------
[Lab 6, Task 15]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-29"
-------------------------------------------------------
"""

# import
from functions import statistics

# input
n = int(input("Enter number of values: "))

# function
minimum, maximum, total, average = statistics(n)

# output
print()
print(f"Minimum: {minimum:.2f}")
print(f"Maximum: {maximum:.2f}")
print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")
