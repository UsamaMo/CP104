"""
-------------------------------------------------------
[Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""

# import
from functions import day_of_week

# input
day_number = int(input("Enter day of week: "))

# function
number = day_of_week(day_number)

# output
print(f'day_of_week({day_number}) -> "{number}"')
