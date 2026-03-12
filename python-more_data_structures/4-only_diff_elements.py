#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for i in set_1:
        is_have = False
        for j in set_2:
            if i == j:
                is_have = True
        if not is_have:
            new_set.add(i)
    return new_set
