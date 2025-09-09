#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    sorted(my_list)
    doing = my_list[0]
    result = my_list[0]
    for i in range(0, len(my_list)):
        if my_list[i] > doing:
            result += my_list[i]
            doing += 1
    return result
