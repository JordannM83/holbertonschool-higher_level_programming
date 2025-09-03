#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for index in str:
        if ord(index) >= 97 and ord(index) <= 122:
            str_upper = chr(ord(index)-32)
        else:
            str_upper = index
        print(str_upper, end="")
    print("")
