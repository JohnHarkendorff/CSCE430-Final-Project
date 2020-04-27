class MainMemory:
    def __init__(self, size, block_size, access_time):
        self.size = size
        self.block_size = block_size
        self.access_time = access_time
        self.total_access_time = 0
        
    def request_data(self, data_value):
        self.total_access_time = self.total_access_time + self.access_time
        return True
        
class Cache:
    def __init__(self, cache_size, block_size, access_time):
        self.cache_size = cache_size
        self.block_size = block_size
        self.max_block_num = int( cache_size / block_size )
        self.access_time = access_time
        self.total_access_time = 0

        self.cache_blocks = []
        
    def request_data(self, data_value):
        self.total_access_time = self.total_access_time + self.access_time
        for value in self.cache_blocks:
            if value == data_value:
                self.update_lru_status(data_value)
                return True
        return False
        
    # data_values is a list of numbers, as opposed to a single number, so that we can easily support
    # adding temporal/spatial values at the same time
    def insert_data(self, data_values):
        for value in data_values:
            if value not in self.cache_blocks:
                # Prepend it to the beginning of the list so we can keep track of the LRU item
                self.cache_blocks.insert(0, value)
            
        # Pop the LRU items if the cache is too full
        while len(self.cache_blocks) > self.max_block_num:
            self.cache_blocks.pop()
        
    # If an item was successfully requested in the cache, we need to update its
    # LRU status and move it to the beginning of the list
    def update_lru_status(self, data_value):
        self.cache_blocks.insert(0, self.cache_blocks.pop(self.cache_blocks.index(data_value)))
