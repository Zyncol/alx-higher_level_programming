#!/usr/bin/python3
# prints a list
def print_matrix_integer(matrix=[[]]):
    r = 0
    while r < len(matrix):
        t = 0
        while t < len(matrix[r]):
            print("{:d}".format(matrix[r][t]), end="")
            if t != (len(matrix[r]) - 1):
                print(" ", end="")
            t += 1
        print("")
        r += 1
