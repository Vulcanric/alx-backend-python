#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Loop 10 times, asynchronously delaying for 1 second  in each iteration

    Args:
        None

    Returns:
        None
    """
    i = 0
    while i < 10:
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
        i += 1
