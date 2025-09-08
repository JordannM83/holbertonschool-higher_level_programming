#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    answer_list = my_list[:]
    for i in range(0, len(my_list) - 1):
        if my_list[i] % 2 == 0:
            answer_list[i] = True
        else:
            answer_list[i] = False
    return answer_list
