#!/usr/bin/env python3
"""
Type Checking
"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """
    Function zoom_array:
        Returns: a list
    """
    zoomed_in: List[Any] = [item for item in lst for _ in range(factor)]
    return zoomed_in
