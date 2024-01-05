#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no argument"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    The coroutine will loop 10 times, each time asynchronously wait 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
