#!/usr/bin/env python3
"""Redis basic operations module"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count method calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


class Cache:
    """Cache class for Redis operations"""

    def __init__(self):
        """Initialize the Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return a key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get data from Redis and convert it if necessary"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Get a string from Redis"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Get an int from Redis"""
        return self.get(key, fn=int)


def replay(method: Callable):
    """Display the history of calls of a particular function"""
    key = method.__qualname__
    inputs = method.__self__._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = method.__self__._redis.lrange(f"{key}:outputs", 0, -1)
    print(f"{key} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{key}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")
