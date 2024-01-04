#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no argument"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator [int, float , None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
