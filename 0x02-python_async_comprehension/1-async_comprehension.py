#!/usr/bin/env python3
"""A coroutine called async_comprehension that takes no argument.
Collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers"""
    random_num = [i async for i in async_generator()]
    return random_num
