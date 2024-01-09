#!/usr/bin/python3
"""
appending a text
"""


def append_write(filename="", text=""):
    """Appending  string at the end of a text file (UTF8)
    Args:
        filename: file to be written
        text: the word
    Return:
          the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as fil:
        count = fil.write(text)

    return count
