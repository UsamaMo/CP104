"""
-------------------------------------------------------
[Lab 5 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-30"
-------------------------------------------------------
"""
import math
# constants
FULL_10YRS = 0.05
FULL_4YRS = 0.015
PART_10YRS = 0.03
PART_4YRS = 0.01
OTHERS = 0.02

INFANT = 3
SENIOR = 65
STUDENT = 10
ADULT = 18

# functions


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """

    if year == day * month:
        magic = True
    else:
        magic = False
    return magic


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """

    if abs(target - v1) > abs(target - v2):

        result = v2
    else:
        result = v1

    return result


def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """

    if n == 1:
        numeral = "I"

    elif n == 2:
        numeral = "II"

    elif n == 3:
        numeral = "III"

    elif n == 4:
        numeral = "IV"

    elif n == 5:
        numeral = "V"

    elif n == 6:
        numeral = "VI"

    elif n == 7:
        numeral = "VII"

    elif n == 8:
        numeral = "VIII"

    elif n == 9:
        numeral = "IX"

    elif n == 10:
        numeral = "X"

    else:
        numeral = "None"

    return numeral


def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """

    if status == "F" and years >= 10:
        new_salary = (FULL_10YRS * salary) + salary

    elif status == "F" and years < 4:
        new_salary = (FULL_4YRS * salary) + salary

    elif status == "P" and years > 10:
        new_salary = (PART_10YRS * salary) + salary

    elif status == "P" and years < 4:
        new_salary = (PART_4YRS * salary) + salary

    else:
        new_salary = (OTHERS * salary) + salary

    return new_salary


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """

    age = int(input("How old are you? "))

    if age < INFANT:
        price = 0

    elif age >= SENIOR:
        price = 4

    elif STUDENT <= age < ADULT:
        student = input("Are you a student at this school? (Y/N): ")

        if student == "Y":
            price = 1

        else:
            price = 3

    elif ADULT <= age < SENIOR:
        price = 5

    elif INFANT <= age < STUDENT:
        price = 2

    return price
