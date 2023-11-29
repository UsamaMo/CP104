"""
-------------------------------------------------------
[Assignment 1, Task5 ]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-09-22"
-------------------------------------------------------
"""

# variables
p = float(input("Principal: $"))
r = float(input("Interest (decimal):"))
t = int(input("Number of years:"))
n = int(input("Number of times interested compounded per year:"))

# compound interest formula
a = p * (1 + (r / n))**(n * t)

print("Balance: $", f"{a: 0.2f}")
