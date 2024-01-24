#!/usr/bin/python3

"""Module holds the cache class."""


import uuid
import redis
from typing import Union


class Cache:
    """Cache class."""
    def __init__(self):
        """Initialize an instance of Cache."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key and return key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
    """Retrieve value stored under input key,
    return it after applying input callable."""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve the value stored under the input key,return it as a str."""
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve value stored under input key, return it as an int."""
        return self.get(key, fn=lambda x: int(x))
