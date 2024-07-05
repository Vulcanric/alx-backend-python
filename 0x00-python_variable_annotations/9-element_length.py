#!/usr/bin/env python3
"""
Type-annotate a function
"""
from typing import Iterable, Sequence, List, Tuple


# From
#
# def element_length(lst):
#   return [(i, len(i)) for i in lst]
#
# To
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function element_length():
        Takes in an iterable(list, tuple, set) containing a
        sequence of any data. And returns...
    Returns: A list(Iterable) containing tuples consisting of
        sequence of any data and an integer.
    """
    return [(i, len(i)) for i in lst]
