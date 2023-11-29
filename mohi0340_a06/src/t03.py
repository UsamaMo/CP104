"""
-------------------------------------------------------
[Assignment 5, Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-15"
-------------------------------------------------------
"""

# Imports
from functions import interest_table

# input
principal = float(input("Principal: $"))
rate = float(input("Interest rate: "))
payment = float(input("Monthly payment: $"))

# output
print()
print(f"interest_table({principal:.0f},{rate:.0f},{payment:.0f}) ->")

# function
interest_table(principal, rate, payment)
