#!/usr/bin/python3
# deletes keys at a value
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for zil, val in a_dictionary.items():
            if val == value:
                del a_dictionary[zil]
                break
    return (a_dictionary)
