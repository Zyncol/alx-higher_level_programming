#!/usr/bin/python3
"""
writing to file module
"""


def write_file(filename="", text=""):
    """jots a string to a text file (UTF8)
    Args:
        filename: file to be written
        text: a written text
    Return:
          the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as fil:
        count = fil.write(text)

    return count
