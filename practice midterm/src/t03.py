"""
-------------------------------------------------------
[task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-30"
-------------------------------------------------------
"""

from functions import sum_all

start = int(input("Enter the start: "))
finish = int(input("Enter the end: "))
increment = int(input("Enter the in increment: "))

total = sum_all(start, finish, increment)

print(
    f"The sum of all numbers from {start} to {finish} increment {increment} is: {total}")
