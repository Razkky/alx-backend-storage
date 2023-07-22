#!/usr/bin/env python3
"""This script stores data in redit and return it key"""
from uuid import uuid4
import redis
from typing import Union


class Cache:
    """A class that operates a caching system using redit"""
    
    def __init__(self):
        """Initialize the redit instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Takes a data and generate a uuid as the key and the data as its value"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, int, float, bytes]:
        """Return data to a key converted to a particular format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """Convert bytes to str"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """Convert bytes to int"""
        return int.from_bytes(data, byteorder)
