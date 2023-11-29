"""
-------------------------------------------------------
[Lab 3, Task 7]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-01"
-------------------------------------------------------
"""
# input
cost_breakfast = float(input("Enter cost of breakfast: $"))
cost_lunch = float(input("Enter cost of lunch: $"))
cost_supper = float(input("Enter  cost of supper: $"))
# formula of total
cost_total = cost_breakfast + cost_lunch + cost_supper
# print total cost
print(f"Meal         Cost")
print(f"Breakfast  ${cost_breakfast: >6.2f}")
print(f"Lunch      ${cost_lunch: >6.2f}")
print(f"Supper     ${cost_supper: >6.2f}")
print(f"(Total     ${cost_total: >6.2f}")
