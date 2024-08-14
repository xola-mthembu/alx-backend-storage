#!/usr/bin/env python3
"""
Main file for testing Cache class methods
"""

Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value, f"Test case failed for value: {value}"

print("All test cases passed!")
