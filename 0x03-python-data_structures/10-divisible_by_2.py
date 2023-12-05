#!/usr/bin/python3
# finds multiples of 2 in list
def divisible_by_2(my_list=[]):
    mult = []
    for r in range(len(my_list)):
        if my_list[r] % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)
    return (mult)
