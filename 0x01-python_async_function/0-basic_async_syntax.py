#!/usr/bin/env python3
""" The basics of async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and max_delay

    Args:
        max_delay (default=10): The maximum amount of seconds to delay

    Returns:
        The number of seconds delayed in floats
    """
    # Get the random number between 0 and max_delay as floats
    random_delay = random.uniform(0, max_delay)

    # Asyncly wait for that number of seconds
    await asyncio.sleep(random_delay)

    # Return the random number
    return random_delay
