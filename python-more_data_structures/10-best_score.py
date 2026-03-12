#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        flag = True
        for key in a_dictionary:
            if flag:
                best_value = a_dictionary[key]
                result = key
                flag = False
            if a_dictionary[key] > best_value:
                best_value = a_dictionary[key]
                result = key
        return result
    else:
        return None
