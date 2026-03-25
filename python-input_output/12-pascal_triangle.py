#!/usr/bin/python3
"""
this module contains a function and this function returns
pascal's triangle depend on n variable's value if n <=0 then
function returns an empty list
"""


def pascal_triangle(n):
    """
    this function returns pascal's triangle depend on n variable's
    value if n<= 0 then function return an empty list
    """
    triangle = []
    last_row = [1]
    if n <= 0:
        return []

    triangle.append(last_row)
    for i in range(n-1):
        current_row = []
        for j in range(i + 2):
            if j == 0 or j == i + 1:
                current_row.append(last_row[0])
            else:
                current_row.append(last_row[j] + last_row[j-1])
        last_row = current_row
        triangle.append(current_row)
    return triangle
