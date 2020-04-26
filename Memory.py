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
                return True
        return False
        
    def insert_data(self, data_value):
        self.cache_blocks.insert(0, data_value)
        if len(self.cache_blocks) > self.max_block_num:
            self.cache_blocks.pop()
