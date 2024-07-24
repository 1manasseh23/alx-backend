#!/usr/bin/env python3
"""This  a class BasicCache that inherits from
BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
     BasicCache class that inherits from BaseCaching
     This caching system has no limit and allows you to
     store key-value pairs without restriction
     """

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
