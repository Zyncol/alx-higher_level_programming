#!/usr/bin/python3
# prints x elements of a list
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for le in range(0, x):
        try:
            print("{:d}".format(my_list[le]), end="")
            cont += 1
        except (ValueError, TypeError):
            pass
    print()
    return cont
