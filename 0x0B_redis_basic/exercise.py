#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:

    def __init__(self):
        """
        Initilize Cache class a Redis client instance and flushes the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
        if fn is None:
            return None

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
