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
        return True

class CacheBlock:
    def __init__(self, data_value): 
        # This will be a number between 0 and the size of the cache. The value can only occur once for each cache level
        self.last_used = 0
        self.data_value = data_value