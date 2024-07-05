#!/usr/bin/env python3
"""
Defines a type-annotated function, `sum_mixed_list` which takes a list
`mxd_list` of integers and floats as argument
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Function sum_mixed_list - Computes the sum of ints and floats in a list
    :param mxd_list: List of ints and floats
    Returns: The sum
    """
    return sum(mxd_list)
