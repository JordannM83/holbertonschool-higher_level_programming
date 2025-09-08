#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest_num = None
    if not my_list:
        return None
    for i in range(0, len(my_list) - 1):
        if biggest_num is None or my_list[i] > biggest_num:
            biggest_num = my_list[i]
    return biggest_num
