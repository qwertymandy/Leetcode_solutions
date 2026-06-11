from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to mark it as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and mark it as most recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        # Check if the cache has exceeded its maximum capacity
        if len(self.cache) > self.capacity:
            # Pop the first element (the least recently used)
            self.cache.popitem(last=False)
