"""
-------------------------------------------------------
[Assignment 7  Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-22"
-------------------------------------------------------
"""

# Task 1


def list_factors(num):
    """
    -------------------------------------------------------
    Takes integer greater than 0 as parameter and returns a
    list of factors that make up that integer
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        factors - list of numbers (list)
    ------------------------------------------------------
    """
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    return factors

# Task 2


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    numbers = []

    num = int(input("Enter a positive number: "))

    while num != 0:
        if num >= 1:
            numbers.append(num)
        num = int(input("Enter a positive number: "))
    print(numbers)

    return numbers

# Task 3


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []

    for i in range(len(values)):
        if values[i] == target:
            locations.append(i)

    return locations

# Task 4


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in subtrahend:
        while i in minuend:
            index = minuend.index(i)
            minuend.pop(index)
    return

# Task 5


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """

    index = -1
    i = 1
    in_order = True
    while in_order and i < len(values):
        if values[i] < values[i - 1]:
            in_order = False
            index = i
        i += 1

    return in_order, index
