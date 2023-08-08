#!/usr/bin/env python3
"""The Module demostrates Async Comprehensions"""

import asyncio
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Function returns 10 random numbers"""

    random_numbers = [number async for number in async_generator()]
    return random_numbers
