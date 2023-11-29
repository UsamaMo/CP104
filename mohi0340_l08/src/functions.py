"""
-------------------------------------------------------
[Lab 8 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""

# import
from random import randint

# functions


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """

    days = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
    name = days[d - 1]
    return name


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values = []
    for _ in range(n):
        values.append(randint(low, high))

    return values


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    smallest = values[0]
    largest = values[0]
    total = 0
    average = 0
    num = (len(values))

    for i in range(num):
        if values[i] > largest:
            largest = values[i]
        elif values[i] < smallest:
            smallest = values[i]
        total += values[i]
    average = total / num

    return smallest, largest, total, average


def linear_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns its index.
    Use: index = linear_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        index - the index of the location of v in a, -1 if not found (int).
    -------------------------------------------------------
    """

    index = -1
    found = False
    i = 0

    while i != len(a) and found == False:
        if v == a[i]:
            index = i
            found = True

        i = i + 1

    return index


def min_search(a):
    """
    -------------------------------------------------------
    Searches through a for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes a has at least
    one element.)
    Use: indexes = min_search(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
    Returns:
        indexes - a list of indexes of the minimum values in
            a (list of int).
    -------------------------------------------------------
    """

    indexes = []
    size = len(a)
    for i in range(0, size):
        if a[i] == min(a):
            indexes.append(i)

    return indexes
