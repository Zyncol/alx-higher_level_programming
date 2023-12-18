#!/usr/bin/python3
# divides element by element 2 lists
def list_division(my_list_1, my_list_2, list_length):
    ans = []
    initialResult = 0
    for li in range(0, list_length):
        try:
            initialResult = my_list_1[li] / my_list_2[li]
        except TypeError:
            initialResult = 0
            print("wrong type")
        except ZeroDivisionError:
            initialResult = 0
            print("division by 0")
        except IndexError:
            initialResult = 0
            print("out of range")
        finally:
            pass
        ans.append(initialResult)
    return ans
