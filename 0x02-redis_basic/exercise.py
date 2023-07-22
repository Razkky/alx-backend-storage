#!/usr/bin/env python3
"""This script stores data in redit and return it key"""
from uuid import uuid4
import redis
from functools import wraps
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """Count the number of calls to Cache class methods"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function for method that increment the key"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """A wrap fucntion that records the history of method
        Calls in the redis fuction
    """
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """A wrapper fucntion to map the call history"""
        input_key = f"{key}:inputs"
        output_key = f"{key}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper

class Cache:
    """A class that operates a cachingj system using redit"""
    
    def __init__(self):
        """Initialize the redit instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data and generate a uuid as the key and the data as its value"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, int, float, bytes]:
        """Return data to a key converted to a particular format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    @count_calls
    def get_str(self, data: bytes) -> str:
        """Convert bytes to str"""
        return data.decode('utf-8')

    @count_calls
    def get_int(self, data: bytes) -> int:
        """Convert bytes to int"""
        return int.from_bytes(data, byteorder)
