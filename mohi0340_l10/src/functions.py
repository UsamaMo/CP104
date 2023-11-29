"""
-------------------------------------------------------
[Lab 10, Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""

# Task 1


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """

    lines = fh.read().split("\n")

    if n < len(lines):
        result = lines[n].strip().split(",")
    else:
        result = []
    return result

# Task 5


def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    for i in range(0, len(fields)):
        if(i == 4):
            print("{}".format(fields[i]), file=fh, end='')
        else:
            print("{}".format(fields[i]), file=fh, end=',')
    return

# Task 6


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """

    line = (fh.readline())
    smallest = None
    largest = None
    total = 0
    count = 0

    while line != "":
        num = int(line)
        if not smallest or num < smallest:
            smallest = num
        if not largest or num > largest:
            largest = num
        total = total + num
        count = count + 1
        line = fh.readline()
    average = total / count

    return smallest, largest, total, average

# Task 10


def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    count = 0
    fh.seek(0)
    line = fh.readline()
    x = line.strip()
    while line != "":
        if(x == word):
            count += 1
        line = fh.readline()
        x = line.strip()
    return count

# Task 13


def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    fh_1.seek(0)
    line = fh_1.readline()
    while line != "":
        print("{}".format(line), file=fh_2, end="")
        line = fh_1.readline()

    return
