#!/usr/bin/python3
"""
Defines a type-annotated function, `make_multiplier`. It takes in a float
`multiplier` as argument and returns a function that multiplies a float
by the `multiplier`
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier(multiplier: float) -> Callable[[float], float]:
        Returns a callable object which multiplies `multiplier` by a
        float passed to it as an argument.
    """
    def multiplier_func(n: float) -> float:
        """
        multiplier_func(n: float) -> float:
            Returns a float as the result of multiplying `n` by `multiplier`
        """
        return multiplier * n
    return multiplier_func
