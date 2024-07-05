#!/usr/bin/env python3
"""
Augmented the following code with the correct duck-typed annotations
"""
from typing import Sequence, Any, Union


# From
#
# def safe_first_element(lst):
#    if lst:
#        return lst[0]
#    else:
#        return None
#
# To
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
