#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    translate = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D" : 500, "M": 1000}
    if not roman_string:
        return 0
    for char in roman_string:
        for let, num in translate.items():
            if let == char:
                result += num
    return result
