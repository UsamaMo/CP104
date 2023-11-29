"""
-------------------------------------------------------
[Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-30"
-------------------------------------------------------
"""
# import
from functions import sum_even

# input
num = int(input("Enter a number: "))

# functions
total = sum_even(num)

# output
print(f"The sum of all even numbers from 2 to {num} is: {total}")
