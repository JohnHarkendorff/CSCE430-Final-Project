#!/usr/bin/env python
import sys

from Memory import MainMemory
from Memory import Cache
from RequestGenerator import RequestGenerator

# Cache sizes, all need to be multiples of CACHE_BLOCK_SIZE
CACHE_BLOCK_SIZE = 2**4                 # 16 bytes per block
L1_SIZE = CACHE_BLOCK_SIZE * ( 2 ** 5 ) # 32 blocks in L1
L2_SIZE = CACHE_BLOCK_SIZE * ( 2 ** 7 ) # 128 blocks in L2
L3_SIZE = CACHE_BLOCK_SIZE * ( 2 ** 9 ) # 512 blocks in L3

# Cache access times, in nanoseconds
L1_ACCESS_TIME = 10
L2_ACCESS_TIME = 50
L3_ACCESS_TIME = 150
MAIN_MEM_ACCESS_TIME = 600

# Constants to be input later
MAX_ADDRESS_VALUE = 2**16 #simulate 16 bit address

if __name__ == "__main__":
    print('\nOption 1:')
    print('Cache Levels: L1')

    print('\nOption 2:')
    print('Cache Levels: L1 and L2')

    print('\nOption 2:')
    print('Cache Levels: L1, L2, and L3')

    cache_size = int(input("Please enter if you want option 1, 2, or 3: "))

    caches = []
    if cache_size == 1:
        caches.append(Cache(L1_SIZE, CACHE_BLOCK_SIZE, L1_ACCESS_TIME))
        caches.append(MainMemory(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, MAIN_MEM_ACCESS_TIME))
    elif cache_size == 2:
        caches.append(Cache(L1_SIZE, CACHE_BLOCK_SIZE, L1_ACCESS_TIME))
        caches.append(Cache(L2_SIZE, CACHE_BLOCK_SIZE, L2_ACCESS_TIME))
        caches.append(MainMemory(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, MAIN_MEM_ACCESS_TIME))
    elif cache_size == 3:
        caches.append(Cache(L1_SIZE, CACHE_BLOCK_SIZE, L1_ACCESS_TIME))
        caches.append(Cache(L2_SIZE, CACHE_BLOCK_SIZE, L2_ACCESS_TIME))
        caches.append(Cache(L3_SIZE, CACHE_BLOCK_SIZE, L3_ACCESS_TIME))
        caches.append(MainMemory(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, MAIN_MEM_ACCESS_TIME))

    request_generator = RequestGenerator(MAX_ADDRESS_VALUE)
    requests = request_generator.generate_requests(1000)
    
    for data_value in requests:
        # First find the requeste piece of data
        data_found = False
        i = 0
        while not data_found and i < len(caches):
            data_found = caches[i].request_data(data_value)
            if not data_found:
                i = i + 1
            
        # After the data has been found, place it in each cache above the one it was found in
        i = i - 1
        while i >= 0:
            caches[i].insert_data(data_value)
            i = i - 1
            
    # Find the access time at the end of making all requests
    total_access_time = 0
    for cache in caches:
        total_access_time = total_access_time + cache.total_access_time
        
    print("Total access time: ", total_access_time)
    print(caches[0].cache_blocks)
    
