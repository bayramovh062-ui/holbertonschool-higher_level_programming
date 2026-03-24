#!/usr/bin/env python3
"""
this module about add and remove methods in classes
"""


class VerboseList(list):
    """
    this class used for testing add remove process but overridding
    with new message
    """
    def append(self, item):
        """
        this function added new element to list but
        same time prints a message
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        this function added new item to list with message
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items")

    def remove(self, value):
        """
        this function remove an element from list by its value
        and prints a message
        """
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=-1):
        """
        this function remove an element from list
        by its index and prints a message
        """
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)
