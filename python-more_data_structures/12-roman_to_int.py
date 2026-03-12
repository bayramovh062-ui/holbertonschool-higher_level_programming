#!/usr/bin/python3
def roman_to_int(roman_string):
    if  isinstance(roman_string, str):
        value_object = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(0, len(roman_string)):
            if i != len(roman_string) - 1:
                if value_object[roman_string[i]] >= value_object[roman_string[i + 1]]:
                    result += value_object[roman_string[i]]
                else:
                    result = result + (value_object[roman_string[i + 1]] - value_object[roman_string[i]])
                    result -= value_object[roman_string[i + 1]]
            else:
                result += value_object[roman_string[i]]
        return result
    else:
        return 0
