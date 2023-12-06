#!/usr/bin/python3
# weighted average of ints
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    aver = 0
    siz = 0
    for visi in my_list:
        aver += (visi[0] * visi[1])
        siz += visi[1]
    return (aver / siz)
