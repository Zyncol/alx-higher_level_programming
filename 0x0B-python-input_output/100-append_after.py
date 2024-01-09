#!/usr/bin/python3
"""
100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a text to a file on with single
    lines
    """
    wor = ""

    with open(filename, "r", encoding="utf-8") as f:
        for mzere in f:
            wor += mzere
            if search_string in mzere:
                wor += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(wor)
