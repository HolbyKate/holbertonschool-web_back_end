#!/usr/bin/python3
"""
Create a class LRUCache that inherits from BaseCaching and is caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Create class"""
    def __init__(self):
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """Assign the item value for key cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = self.cache_keys.pop(0)
            print(f"DISCARD: {discard_key}")
            del self.cache_data[discard_key]

        self.cache_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Return the value giving with key in the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_keys.remove(key)
        self.cache_keys.append(key)
        return self.cache_data[key]
