class Cache:
    def __init__(self, cache_size, block_size, next_level_cache, main_mem_flag = False):
        # Stats about the cache itself
        self.cache_size = cache_size
        self.block_size = block_size
        self.max_block_num = int( cache_size / block_size )
        self.access_count = 0

        # Reference to the next deepest cache
        self.next_level_cache = next_level_cache

        # Init cache blocks, if main mem, fill all
        self.cache_blocks = []
        self.main_mem_flag = main_mem_flag
        if main_mem_flag:
            # Init all cache blocks in address space
            for i in range(self.max_block_num):
                # Calculate starting and ending address of block
                start = i * self.block_size
                end = (i+1) * self.block_size - 1
                self.cache_blocks.append( CacheBlock( start, end ) )

    # Human readable version of the cache
    def __str__(self):
        stringified = ""

        if self.main_mem_flag:
            stringified += "\n<MainMemory>"
        else:
            stringified += "\n<Cache>"

        stringified += " size: {}, block size: {}, max number of blocks: {}, current number of blocks: {}".format(self.cache_size, self.block_size, self.max_block_num, len(self.cache_blocks) )
        stringified += ", accesses: {}".format( self.access_count )

        return stringified

    def search_for_address(self, mem_address):
        # Cache is being searched, increment access count
        self.access_count += 1

        # Search each block for the address, if found, return copy
        for block in self.cache_blocks:
            if block.contains_address(mem_address):
                block.set_last_access(self.access_count)
                return CacheBlock(block.min_address, block.max_address)
        
        # If we hit the bottom of all caches, return false, value not found
        if self.next_level_cache is None:
            return False

        # If address not contained in any blocks, search cache below
        found = self.next_level_cache.search_for_address(mem_address)

        # If not found below, there is a problem
        if not found:
            return False
        
        # Block was found below, move this block into our current cache then return a copy
        found.set_last_access(self.access_count)
        self.cache_new_block(found)
        return CacheBlock(found.min_address, found.max_address)

    def cache_new_block(self, block_to_cache):
        # If this cache is not yet full, simply add block
        if len(self.cache_blocks) < self.max_block_num:
            self.cache_blocks.append( block_to_cache )

        # If this cache is full, decide which block to evict
        else:
            least_recent_ind = 0
            least_recent_val = float("inf")

            # Find least recently used block
            for i in range(0, len(self.cache_blocks)):
                block = self.cache_blocks[i]
                if block.last_access_count < least_recent_val:
                    least_recent_ind = i
                    least_recent_val = block.last_access_count
            
            # Swap in new block for least recently used block
            self.cache_blocks[i] = block_to_cache

class CacheBlock:
    def __init__(self, min_address, max_address):	
        self.min_address = min_address
        self.max_address = max_address
        self.last_access_count = 0

    def contains_address(self, mem_address):
        return mem_address >= self.min_address and mem_address <= self.max_address

    def set_last_access(self, new_access_count):
        self.last_access_count = new_access_count