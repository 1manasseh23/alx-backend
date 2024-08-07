#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Defines a LFU caching system """

    def __init__(self):
        """ Initialize the LFUCache instance """
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # Check if key already exists
        if key in self.cache_data:
            # Update existing key's item
            self.cache_data[key] = item
            # Increase frequency count
            self.frequency[key] += 1
        else:
            # Add new key to cache
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the item(s) with the minimum frequency
                min_freq = min(self.frequency.values())
                items_with_min_freq = [
                        k for k, v in self.frequency.items() if v == min_freq]

                # If there are ties, use LRU to discard
                if len(items_with_min_freq) > 1:
                    lru_key = min(
                            self.usage_order,
                            key=lambda k: self.usage_order.index(k)
                            )
                    del self.cache_data[lru_key]
                    self.usage_order.remove(lru_key)
                    del self.frequency[lru_key]
                    print(f"DISCARD: {lru_key}")
                else:
                    discard_key = items_with_min_freq[0]
                    del self.cache_data[discard_key]
                    del self.frequency[discard_key]
                    print(f"DISCARD: {discard_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1

        # Update usage order for LRU
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None:
            return None

        if key in self.cache_data:
            # Increase frequency count
            self.frequency[key] += 1
            # Update usage order for LRU
            if key in self.usage_order:
                self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        else:
            return None
