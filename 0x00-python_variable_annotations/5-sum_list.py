#!/usr/bin/env python3
"""
Defines a type-annotated function, `sum_list` which takes a list `input_list`
of floats as argument
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function sum_list - Computes the sum of floats in a list
    :param input_list: List of floats
    Returns: The sum
    """
    return sum(input_list)
