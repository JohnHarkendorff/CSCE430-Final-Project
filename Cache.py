class Cache:
    def __init__(self, cache_size, block_size, main_mem_flag = False):
        self.cache_size = cache_size
        self.block_size = block_size
        self.max_block_num = int( cache_size / block_size )

        self.cache_blocks = []

        if main_mem_flag:
            for i in range(self.cache_size):
                self.cache_blocks.append(CacheBlock(i))

class CacheBlock:
    def __init__(self, data_value):	
        # This will be a number between 0 and the size of the cache. The value can only occur once for each cache level
        self.last_used = 0
        self.data_value = data_value