"""
-------------------------------------------------------
[Lab 10, Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""

# Imports
from functions import customer_record

# file location
file_1 = "customers.txt"

print("Find record n")

# file
fh = open(file_1)

# input
n = int(input("Enter a record number: "))

# function
result = customer_record(fh, n)

# output
print(result)
