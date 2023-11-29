"""
-------------------------------------------------------
[Assignment 3 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-10-18"
-------------------------------------------------------
"""
# import
from random import randint

# constants
VALUE = 43560

# functions


def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """

    acres = square_footage / VALUE

    return acres


def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """

    time = (width * length) / speed

    return time


def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """

    day = (date_number % 1000000) // 10000
    month = date_number // 1000000
    year = date_number % 10000

    return year, month, day


def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    num_total = (num1 * num2)
    denom_total = (denom1 * denom2)

    product = num_total / denom_total

    return num_total, denom_total, product


def math_quiz():
    """
    -------------------------------------------------------
    Use: numerator,denominator,sum= math_quiz(num1,num2)
    num1= random integer between 0 to 999
    num2= random integer between 0 to 999
    -------------------------------------------------------
    Parameters:
    -no parameters
    Returns:
    -no return values
    ------------------------------------------------------
    """

    num1 = randint(0, 999)
    num2 = randint(0, 999)

    expected_num = num1 + num2

    print(f"{num1}")
    print(f"+{num2}")
    print()

    answer = int(input("Your answer:"))

    print()
    print(f"Your answer:{answer: >5}")
    print(f"Expected:{expected_num: >8}")

    return
