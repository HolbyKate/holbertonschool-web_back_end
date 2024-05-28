#!/usr/bin/python3
"""
Create a class BasicCache that inherits from BaseCaching and is caching system
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Add a key and see if it's none or not"""
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item
            
    def get(self, key):
        """return the value in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
