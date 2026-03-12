#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        value_object = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(0, len(roman_string)):
            curr_value = value_object[roman_string[i]]
            next_value = value_object[roman_string[i + 1]]
            if i != len(roman_string) - 1:
                if curr_value >= next_value:
                    result += curr_value
                else:
                    result = result + (next_value - curr_value)
                    result -= next_value
            else:
                result += curr_value
        return result
    else:
        return 0
