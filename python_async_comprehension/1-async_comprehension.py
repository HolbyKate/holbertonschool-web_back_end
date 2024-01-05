#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments
"""

import asyncio
import random
import time
from typing import AsyncGenerator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Create an asynchronous list comprehension and return the list"""
    result = [i async for i in async_generator()]
    return result
