"""
-------------------------------------------------------
[Assignment 2, Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-04"
-------------------------------------------------------
"""

# inputs
num_balloon = int(input("Number of balloons: "))
num_children = int(input("Number of children: "))

#modulus and remainder
total_balloon = num_balloon // num_children
leftover_balloon = num_balloon % num_children

# output
print(" ")
print(f"Each child receives {total_balloon} balloons")
print(f"Balloons that won't be distributed: {leftover_balloon}")
