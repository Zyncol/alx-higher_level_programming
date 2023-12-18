#!/usr/bin/python3
# prints elements of a list
def safe_print_list(my_list=[], x=0):
    sam = 0
    for li in range(x):
        try:
            print(f"{my_list[li]}", end="")
            sam += 1
        except IndexError:
            break
    print()
    return(sam)
