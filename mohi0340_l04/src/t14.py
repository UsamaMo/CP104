"""
-------------------------------------------------------
[Lab 4, Task 14]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-08"
-------------------------------------------------------
"""

# Import
from functions import time_values

# Input
seconds = int(input("Number of Seconds:"))

print("")

# function
days, hours, minutes = time_values(seconds)

# Output
print(f"{seconds} seconds is the same as:")
print(f"  {days} days")
print(f"  {hours} hours")
print(f"  {minutes} minutes")
