#!/usr/bin/env python3
""" A type-annotated function that takes a string k and
an int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple of the string & square of v as float"""
    return (k, float(v)**2)
