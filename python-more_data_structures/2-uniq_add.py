#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted(my_list)
    doing = 0
    result = 0
    for i in range(0, len(my_list)):
        if my_list[i] > doing:
            result += my_list[i]
            doing += 1
    return result
