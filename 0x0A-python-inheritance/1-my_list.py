#!/usr/bin/python3
"""
Defines an inherited list class MyList
print in a list in ascending order
"""


class MyList(list):
    """
    class list been inheridted
    """
    def print_sorted(self):
        """to be printed in ascending"""
        print(sorted(self))
