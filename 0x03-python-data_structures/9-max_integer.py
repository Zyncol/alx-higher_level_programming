#!/usr/bin/python3
# prints biggest integer
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    big = my_list[0]
    for r in range(len(my_list)):
        if my_list[r] > big:
            big = my_list[r]
    return big
