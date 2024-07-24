#!/usr/bin/env python3
"""
Module for BasicCache class that inherits from BaseCaching
"""


BaseCaching = __import__('0-basic_cache').BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system that doesn't have a limit.
    """
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
