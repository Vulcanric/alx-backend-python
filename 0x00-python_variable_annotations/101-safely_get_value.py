#!/usr/bin/env python3
"""
Type-annotates the function
"""
from typing import Mapping, Any, Union, TypeVar, Optional


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Optional[T] = None
                     ) -> Any | T:
    """
    Done: ye done!
    """
    if key in dct:
        return dct[key]
    else:
        return default
