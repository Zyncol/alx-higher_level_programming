#!/usr/bin/python3
le = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - le)), end="")
    le = 32 if le == 0 else 0
