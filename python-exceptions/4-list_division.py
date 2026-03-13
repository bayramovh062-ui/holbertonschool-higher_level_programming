#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    division_error_message = "division by 0"
    typeErrorMessage = "wrong type"
    indexErrorMessage = "out of range"
    is_have_division = False
    is_have_type = False
    is_have_index = False
    flag = False
    try:
        for i in range(0, list_length):
            try:
                 if my_list_2[i] == 0:
                    is_have_division = True
                    flag = True
                new_list.append(my_list_1[i] / my_list_2[i])
            except (ValueError, TypeError, ZeroDivisionError):
                new_list.append(0)
                if not flag:
                    is_have_type = True
                else:
                    flag = False
    except (IndexError):
        is_have_index = True
    finally:
        if is_have_division:
            print(division_error_message)
        if is_have_type:
            print(typeErrorMessage)
        if is_have_index:
            print(indexErrorMessage)
        return new_list
