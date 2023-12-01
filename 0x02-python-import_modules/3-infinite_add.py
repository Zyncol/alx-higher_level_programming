#!/usr/bin/python3
# prints all total
if __name__ == "__main__":
    import sys
    Toto = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            Toto += int(arg)
    print(Toto)
