#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments
"""

import asyncio
import random
from typing import Generator, List


async def async_generator() -> Generator[float, None, None]:
    """
    The coroutine will loop 10 times, each time asynchronously wait 1 second
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    The coroutine will collect 10 random numbers using
    an async comprehensing over async_generator
    """
    for i in range(10):
        await asyncio.sleep(1)
        return [i async for i in async_generator()]
