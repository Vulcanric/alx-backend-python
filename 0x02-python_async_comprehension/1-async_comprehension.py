#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehensing over
    coroutine async_generator() from 0-async_generator.py

    Args:
        None

    Returns:
        The 10 random numbers
    """
    async_generator = __import__('0-async_generator').async_generator

    random_numbers = [number async for number in async_generator()]
    return random_numbers
