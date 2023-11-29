"""
-------------------------------------------------------
[Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-30"
-------------------------------------------------------
"""

from functions import sum_partial_harmonic

n = int(input("Enter n: "))

total = sum_partial_harmonic(n)

print(f"The sum of the series 1 to {n} is: {total}")
