#!/usr/bin/python3
# prints dictionary by keys
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(ze, a_dictionary[ze])) for ze in sorted(a_dictionary)]
