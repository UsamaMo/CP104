"""
-------------------------------------------------------
[Task 10]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-30"
-------------------------------------------------------
"""

from functions import treadmill

burnt_per_minute = float(input("ENter calories burned per minute: "))
start = int(input("Beginning num of minutes:"))
end = int(input("ending num of min: "))
inc = int(input("increment: "))

treadmill(burnt_per_minute, start, end, inc)
