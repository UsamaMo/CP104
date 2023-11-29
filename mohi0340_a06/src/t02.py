"""
-------------------------------------------------------
[Assignment 5, Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-15"
-------------------------------------------------------
"""

# Imports
from functions import is_prime

# input
num = int(input("Enter a number greater than 0: "))

# function
prime = is_prime(num)

# output
if prime == True:
    print(f"is_prime({num})->{prime}")

elif prime == False:
    print(f"is_prime({num})->{prime}")
