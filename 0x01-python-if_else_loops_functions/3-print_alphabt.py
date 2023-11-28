#!/usr/bin/python3
le = ord('a')
while le <= ord('z'):
    if le != ord('q') and le != ord('e'):
        print("{}".format(chr(le)), end="")
    le = le + 1
