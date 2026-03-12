#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()

    def full_set(set_1, set_2):
        for i in set_1:
            is_have = False
            for j in set_2:
                if i == j:
                    is_have = True
            if not is_have:
                if i not in new_set:
                    new_set.add(i)
    full_set(set_1, set_2)
    full_set(set_2, set_1)
    return new_set
