#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import time


async def measure_runtime() -> float:
    """
    Executes async_comprehension() from 1-async_comprehensions.py, four times
    in parallel

    Args:
        None

    Returns:
        Measure of runtime
    """
    async_comprehension = __import__('1-async_comprehension').\
        async_comprehension

    start = time.perf_counter()
    await asyncio.gather(
            *[async_comprehension() for i in range(4)]
            )
    stop = time.perf_counter()

    return stop - start
