"""
-------------------------------------------------------
[Lab 4, Task 7]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-08"
-------------------------------------------------------
"""

# Import
from functions import total_change

# Inputs
nickels = float(input("Enter number of nickels:"))
dimes = float(input("Enter number of dimes:"))
quarters = float(input("Enter number of quarters:"))
loonies = float(input("Enter number of loonies:"))
toonies = float(input("Enter number of toonies:"))

# function
total_calculated_change = total_change(
    nickels, dimes, quarters, loonies, toonies)

# Output
print("")
print(f"Total amount: ${total_calculated_change :.2f}")
