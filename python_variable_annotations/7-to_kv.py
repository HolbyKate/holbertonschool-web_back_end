#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """Returns tuple of string and float/int"""
    return (k, v * v)
