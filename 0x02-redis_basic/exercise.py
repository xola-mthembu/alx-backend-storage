#!/usr/bin/env python3
"""Module to implement Redis cache storage"""

import redis
import uuid
from typing import Union


class Cache:
    """Cache class to interact with Redis server"""

    def __init__(self):
        """Initialize the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
