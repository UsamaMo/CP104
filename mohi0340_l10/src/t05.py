"""
-------------------------------------------------------
[Lab 10, Task 5]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""

# imports
from functions import customer_append

# file
fh = open("customers.txt", "a+", encoding="utf-8")

# file input
fields = ['35612', 'David', 'Brown', '237.56', '2008-10-10']

# function
customer_append(fh, fields)

# output
print(f'Data: {fields}')
print("data appended to file")
