"""
-------------------------------------------------------
[Lab 5, Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-22"
-------------------------------------------------------
"""

# import
from functions import magic_date


print("Enter a date.")

# input
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year (2 digits): "))

# function
magic = magic_date(day, month, year)

# output
print()
if magic == True:
    print(f"{day}/{month}/{year} is a magic date.")
else:
    print(f"{day}/{month}/{year} is not a magic date.")
