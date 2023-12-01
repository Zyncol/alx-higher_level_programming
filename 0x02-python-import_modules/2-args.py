#!/usr/bin/python3
# prints the number and arg
if __name__ == "__main__":
    import sys
    ku = len(sys.argv) - 1
    if ku == 0:
        print("{:d} arguments.".format(ku))
    elif ku == 1:
        print("{:d} argument:".format(ku))
    else:
        print("{:d} arguments:".format(ku))
    for c in range(ku):
        print("{}: {}".format(c + 1, sys.argv[c + 1]))
