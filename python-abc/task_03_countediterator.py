#!/bin/usr/env python3
"""
this module extend properties of __next__ method
"""


class CountedIterator():
    """
    this class count Iterators
    """
    def __init__(self, some_iterable):
        """
        this function count values and increase them 
        """
        self.iterator = iter(some_iterator)
        self.counter = 0

    def get_count(self):
        """
        this function return current number of interator
        """
        return self.counter

    def __next__(self):
        """
        fetches next item increase counter and stop when
        counter catch up limit
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
