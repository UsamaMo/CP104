"""
-------------------------------------------------------
[Lab 2, Task 8]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-09-21"
-------------------------------------------------------
"""

# input values
height = float(input("Enter your height (m):"))
weight = float(input("Enter your weight (kg):"))
upperbmi = int(input(
    "Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else):"))

# calculation for bmi
bmi = weight / (height**2)

print(
    "Body Mass Index (kg/m^2)=", bmi)

# calculation for bmiprime
bmiprime = bmi / upperbmi

print(
    "BMI Prime=", bmiprime)
