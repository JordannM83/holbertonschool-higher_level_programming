#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
my_list = [-1, -90, -2, -13, -34, -5, -13, -3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
my_list = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
my_list = [-410, 25, 1, 0, 24, 348]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
my_list = [-410, 25, 1, 0, 24, 3482316852397835679178659132795839687297319678521378952798316978317856213758623967832965782963789523789623789213976832967832967823196783295783216973948237492759627956239456239765296731295739265762376923196753296753129674391657369237546921379642137962]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
