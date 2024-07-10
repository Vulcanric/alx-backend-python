#!/usr/bin/env python3
""" Executes multiple coroutines at the same time with async """
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns function, task_wait_random() with the value of max_delay, for n
    number of times

    Args:
        n (integer): The number of times to execute coroutine
        max_delay (integer): Passed as argument to coroutine

    Returns:
        A list of returned floats, obtained from n calls of coroutine
    """
    task_wait_random = __import__('3-tasks').task_wait_random

    tasks, delays = [], []

    # Add n number of tasks to the tasks list
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    # Yields tasks in order of their completion
    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
