"""
-------------------------------------------------------
[Lab 5, Task 12]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-22"
-------------------------------------------------------
"""

# import
from functions import pay_raise

# input
status = input("Status: ")
years = int(input("Years: "))
salary = float(input("Salary: "))

# function
new_salary = pay_raise(status, years, salary)

# output
print()
print(f"New Salary: ${new_salary:,}")
