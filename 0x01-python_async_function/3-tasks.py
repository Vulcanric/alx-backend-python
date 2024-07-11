#!/usr/bin/env python3
""" Tasks """
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task object

    Arg:
        max_delay (integer): Task(Coroutine) argument

    Returns: an asyncio.Task object
    """
    wait_random = __import__("0-basic_async_syntax").wait_random

    # Create task object from coroutine
    # Used to schedule the execution of a coroutine object
    # Before it is awaited and ran
    task = asyncio.create_task(wait_random(max_delay))
    # await task
    # asyncio.run(task)
    return task
