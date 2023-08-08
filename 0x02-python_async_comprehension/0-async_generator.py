#!/usr/bin/env python3
"""Module contains a function to illustrate async generator"""

import asyncio
import random

async def async_generator():
    """Generate loop 10 times and each asynchronously wait 1s """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
