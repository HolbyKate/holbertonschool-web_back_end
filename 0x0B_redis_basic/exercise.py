#!/usr/bin/env python3

import redis
import uuid
from typing import Union


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