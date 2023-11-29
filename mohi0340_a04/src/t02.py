"""
-------------------------------------------------------
[Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""

# import
from functions import pollution_level

# input
aqi = int(input("Enter EQI Level: "))

# function
level = pollution_level(aqi)

# output
print(f'pollution_level({aqi}) -> "{level}"')
