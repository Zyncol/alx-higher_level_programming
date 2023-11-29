#!/usr/bin/python3
# prints the last digit
def print_last_digit(number):
    last_num = number % 10
    print(last_num, end="")
    return(number % 10)
