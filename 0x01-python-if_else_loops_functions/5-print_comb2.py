#!/usr/bin/python3
for nu in range(0, 100):
    if nu != 99:
        print("{:02}".format(nu), end=", ")
    else:
        print("{}".format(nu))
