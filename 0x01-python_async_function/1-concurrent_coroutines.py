#!/usr/bin/env python3
""" Executes multiple coroutines at the same time with async """
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns coroutine, wait_random() with the value of max_delay, for n
    number of times

    Args:
        n (integer): The number of times to execute coroutine
        max_delay (integer): Passed as argument to coroutine

    Returns:
        A list of returned floats, obtained from n calls of coroutine
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    list_of_delays = [await wait_random(max_delay) for i in range(n)]

    return list_of_delays
