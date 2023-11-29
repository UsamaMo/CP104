"""
-------------------------------------------------------
[Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""
# import
from functions import rgb_mix

# input
rgb1 = str(input("Enter colour 1: "))
rgb2 = str(input("Enter colour 2: "))

# functions
colour = rgb_mix(rgb1, rgb2)

# output
print(f'rgb_mix("{rgb1}", "{rgb2}") -> "{colour}"')
