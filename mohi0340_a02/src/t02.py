"""
-------------------------------------------------------
[Assignment 2 , Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2022-10-06"
-------------------------------------------------------
"""

# constant
BASE = 10

# input
digit = int(input("Enter a positive digit number: "))

#modulus and remainders
digit10 = digit // BASE
digit_r = digit % BASE


# formula
final = digit10 - digit_r


print(f"The difference of the digits of {digit} is {final}")
