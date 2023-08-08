#!/usr/bin/env python3
"""Module to demostrate basics of async"""

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """Cause delay for a random time and returns the delay time.
    arguments
    max_delay - maximum time delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
