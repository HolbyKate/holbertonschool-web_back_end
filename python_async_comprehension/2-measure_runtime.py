#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in parallel
using asyncio.gather
"""


import asyncio
import random
from typing import AsyncGenerator, List
import time


async def async_generator() -> AsyncGenerator[float, None]:
    """
    The coroutine will loop 10 times, each time asynchronously wait 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    The coroutine will collect 10 random numbers using
    an async comprehensing over async_generator
    """
    for i in range(10):
        await asyncio.sleep(1)
        return [_ async for _ in async_generator()]
    return []


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return (end_time - start_time)
