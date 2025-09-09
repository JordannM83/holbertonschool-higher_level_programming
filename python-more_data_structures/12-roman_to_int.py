#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    translate = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}
    if not roman_string or type(roman_string) is not str:
        return 0
    for char in range(0, len(roman_string)):
        if roman_string[char] in translate.keys():
            if (char < len(roman_string) - 1 and
               translate[roman_string[char]]
               < translate[roman_string[char + 1]]):
                result -= translate[roman_string[char]]
            else:
                result += translate[roman_string[char]]
    return result
