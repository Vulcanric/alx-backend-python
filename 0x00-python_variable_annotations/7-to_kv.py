#!/usr/bin/env python3
"""
Defines a type-annotated function, `to_kv` that takes a string `k`
and an int Or float `v` as argument and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """
    Function to_kv:
        Returns a tuple containing (k, v)
    """
    return (k, v)
