"""
-------------------------------------------------------
[Lab 3, Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-01"
-------------------------------------------------------
"""

# input
number = float(input("Enter Number:"))
percent = float(input("Enter Percent:"))

# formula
formula = (percent / 100) * number

# print discount
print(f"A {percent:.1f} percent discount on {number:.1f} is {formula:.1f}")
