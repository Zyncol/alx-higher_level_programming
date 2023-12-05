#!/usr/bin/python3
# the stringss
def no_c(my_string):
    replacing = ''
    for k in my_string:
        if k != 'c' and k != 'C':
            replacing = replacing + k
    return (replacing)
