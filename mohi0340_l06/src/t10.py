"""
-------------------------------------------------------
[Lab 6, Task 10]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-29"
-------------------------------------------------------
"""

# import
from functions import treadmill

# input
burnt_per_minute = float(input("Enter calories burned per minute: "))
start = int(input("Enter beginning number of minutes: "))
end = int(input("Enter ending number of minutes: "))
inc = int(input("Enter the increment in minutes: "))

print()

# function
treadmill(burnt_per_minute, start, end, inc)
