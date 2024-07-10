#!/usr/bin/env python3
""" Measure the runtime """
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of asynchronous coroutine, wait_n() from
    1-concurrent_coroutines.py

    Args:
        n (integer): first argument passed to coroutine.
        max_delay (integer): second argument passed to coroutine

    Returns:
        the total execution time for the coroutine
    """
    # Get asynchronous coroutine
    wait_n = __import__('1-concurrent_coroutines').wait_n

    # Starting time counter
    start = time.perf_counter()
    # Execute asynchronous coroutine
    asyncio.run(wait_n(n, max_delay))

    # Calculate total time
    total_time = start - time.perf_counter()
    runtime = total_time / n

    return runtime.__abs__()
