#!/usr/bin/python3
for h in range(ord('a'), ord('z') + 1):
    if chr(h) != 'q' and chr(h) != 'e':
        print("{}".format(chr(h)), end='')
