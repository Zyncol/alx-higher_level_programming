#!/usr/bin/python3
# prints dictionary by keys
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(zel, a_dictionary[zel])) for zel in sorted(a_dictionary)]
