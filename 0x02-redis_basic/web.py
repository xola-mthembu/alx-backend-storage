#!/usr/bin/env python3
"""Web cache and tracker module"""

import redis
import requests
from functools import wraps
from typing import Callable


def cache_with_expiration(expiration: int = 10) -> Callable:
    """Decorator to cache the result of a function with expiration"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            """Wrapper function"""
            redis_client = redis.Redis()
            key = f"cache:{url}"
            cached_result = redis_client.get(key)

            if cached_result:
                return cached_result.decode('utf-8')

            result = func(url)
            redis_client.setex(key, expiration, result)
            return result
        return wrapper
    return decorator


@cache_with_expiration()
def get_page(url: str) -> str:
    """Get the HTML content of a web page and cache the result"""
    response = requests.get(url)
    redis_client = redis.Redis()
    count_key = f"count:{url}"
    redis_client.incr(count_key)
    return response.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.com"
    print(get_page(url))
    print(get_page(url))
