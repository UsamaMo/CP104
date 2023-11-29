"""
-------------------------------------------------------
[Assignment 8 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:           212090340
Email:     mohi0340@mylaurier.ca
__updated__ = "2021-11-28"
-------------------------------------------------------
"""

# Task  1


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """

    new_string = string[0]

    for ch in string[1:]:
        if ch.isupper():
            new_string += " "

        new_string += ch.lower()

    return new_string

# Task 2


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """

    if string.endswith("s") or string.endswith("sh") or string.endswith("ch"):
        plural = string + "es"
    elif string.endswith("y") and not (string.endswith("ay") or string.endswith("oy")):
        plural = string[:-1] + "ies"
    else:
        plural = string + "s"

    return plural


# Task 3
def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """

    common = ""
    num = len(string1) - 1
    s = string1[num:]

    while num >= 0 and string2.endswith(s):
        common = s
        num -= 1
        s = string1[num:]
    return common

# Task 4


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    groups = isbn.split("-")
    valid = True

    if len(isbn) != 17 or len(groups) != 5:

        valid = False
    else:
        if groups[0] not in ["978", "979"]:
            valid = False
        elif len(groups[4]) != 1:
            valid = False
        else:
            for group in groups:
                if not group.isdigit():
                    valid = False

    return valid

# Task 5


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    letter = word_list[0][-1]
    word_chain = True
    temp = 1

    while word_chain and temp < len(word_list):
        if word_list[temp][0] != letter:
            word_chain = False

        letter = word_list[temp][-1]
        temp += 1

    return(word_chain)
