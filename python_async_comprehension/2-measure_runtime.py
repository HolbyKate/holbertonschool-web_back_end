#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in parallel
using asyncio.gather
"""


import asyncio
import random
from typing import Generator, List
from time import perf_counter


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


async def measure_runtime() -> float:
    """
    Coroutine that will execute async_comprehension four times in parallel
    using asyncio.gathermeasure_runtime should measure the total runtime
    and return it
    """
    start = perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = perf_counter()
    return end - start
