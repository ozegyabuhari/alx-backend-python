#!/usr/bin/env python3
""" An asynchronous coroutine
that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random number of seconds"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
