#!/usr/bin/python3
"""
function read file
"""


def read_file(filename=""):
    """Reads text file  and print it out
    Args:
    filename: textes resides
    Return: 
         none
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for mzere in f:
            print(mzere, end="")
