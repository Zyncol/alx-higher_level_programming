#!/usr/bin/python3
"""
Defines an inherited list class MyList
print in a list in ascending order
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
