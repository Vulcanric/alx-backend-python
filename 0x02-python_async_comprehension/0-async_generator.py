#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.randint(0, 10)
