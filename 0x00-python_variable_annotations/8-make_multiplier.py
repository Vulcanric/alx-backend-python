#!/usr/bin/python3
"""
Defines a type-annotated function, `make_multiplier`. It takes in a float
`multiplier` as argument and returns a function that multiplies a float
by the `multiplier`
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(n: float) -> float:
        return multiplier * n
    return multiplier_func
