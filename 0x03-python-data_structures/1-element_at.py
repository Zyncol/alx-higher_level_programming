#!/usr/bin/python3
# retrieves an element from a list
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list) - 1:
        return (None)
    return(my_list[idx])
