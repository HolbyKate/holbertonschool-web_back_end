#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:

    def __init__(self):
        """
        Initilize Cache class a Redis client instance and flushes the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    """decorate with count_calls"""
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a new uuid and store the data in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes, int, float, None]:
        """
        Retrieve data from Redis using the given key if fn is provided,
        use it to convert the data
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a string value from Redis
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer value from Redis
        """
        return self.get(key, fn=int)
