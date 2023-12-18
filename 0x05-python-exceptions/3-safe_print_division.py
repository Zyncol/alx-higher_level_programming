#!/usr/bin/python3
# prints results of a division
def safe_print_division(a, b):
    try:
        ans = a / b
    except (ZeroDivisionError, FloatingPointError):
        ans = None
    finally:
        print("Inside result: {}".format(ans))
    return ans
