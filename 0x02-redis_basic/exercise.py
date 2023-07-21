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


    def store(self, data: Union[str, int, bytes, float]) -> str :
        """Takes a data and generate a uuid as the key and the data as its value"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key


