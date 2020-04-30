#!/usr/bin/env python
import sys

from Cache import Cache
from Cache import CacheBlock
from RequestGenerator import RequestGenerator

# Probabilities of different types of access
PREV_PROB = 0.1
TEMPORAL_PROB = 0.30
SPATIAL_PROB = 0.50
RANDOM_PROB = 1.0 - PREV_PROB - TEMPORAL_PROB - SPATIAL_PROB

# Cache sizes, all need to be multiples of CACHE_BLOCK_SIZE
CACHE_BLOCK_SIZE = 2**4 				 # 16 bytes per block
L1_SIZE = CACHE_BLOCK_SIZE * ( 2 ** 4 )  # 16 blocks in L1
L2_SIZE = CACHE_BLOCK_SIZE * ( 2 ** 7 )  # 128 blocks in L2
L3_SIZE = CACHE_BLOCK_SIZE * ( 2 ** 10 ) # 1024 blocks in L3

# Cache access times, in nanoseconds
L1_ACCESS_TIME = 10
L2_ACCESS_TIME = 50
L3_ACCESS_TIME = 150
MAIN_MEM_ACCESS_TIME = 600

# Constants to be input later
MAX_ADDRESS_VALUE = 2**16 #simulate 16 bit address

if __name__ == "__main__":

    # Have user select cache option
    print('\nOption 1:')
    print('Cache Levels: L1')

    print('\nOption 2:')
    print('Cache Levels: L1 and L2')

    print('\nOption 2:')
    print('Cache Levels: L1, L2, and L3')

    cache_size = int(input("Please enter if you want option 1, 2, or 3: "))

    # Init selected cache option
    caches = []
    if cache_size == 1:
        caches.insert(0, Cache(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, None, MAIN_MEM_ACCESS_TIME, True))
        caches.insert(0, Cache(L1_SIZE, CACHE_BLOCK_SIZE, caches[0], L1_ACCESS_TIME ) )
    elif cache_size == 2:
        caches.insert(0, Cache(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, None, MAIN_MEM_ACCESS_TIME, True))
        caches.insert(0, Cache(L2_SIZE, CACHE_BLOCK_SIZE, caches[0], L2_ACCESS_TIME ) )
        caches.insert(0, Cache(L1_SIZE, CACHE_BLOCK_SIZE, caches[0], L1_ACCESS_TIME ) )
    elif cache_size == 3:
        caches.insert(0, Cache(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, None, MAIN_MEM_ACCESS_TIME, True))
        caches.insert(0, Cache(L3_SIZE, CACHE_BLOCK_SIZE, caches[0], L3_ACCESS_TIME ) )
        caches.insert(0, Cache(L2_SIZE, CACHE_BLOCK_SIZE, caches[0], L2_ACCESS_TIME ) )
        caches.insert(0, Cache(L1_SIZE, CACHE_BLOCK_SIZE, caches[0], L1_ACCESS_TIME ) )

    # Print results of init
    print("\nNumber of caches: ", len(caches)-1) # minus 1 because memory is the last one
    print("L1 size (in bytes): ", caches[0].cache_size)
    if cache_size >= 2:
        print("L2 size (in bytes): ", caches[1].cache_size)
    elif cache_size == 3:
        print("L2 size (in bytes): ", caches[1].cache_size)
        print("L3 size (in bytes): ", caches[2].cache_size)
    print("Main mem size: ", len(caches[len(caches) - 1].cache_blocks))

    # Generate memory access requests
    request_generator = RequestGenerator(MAX_ADDRESS_VALUE, PREV_PROB, TEMPORAL_PROB, SPATIAL_PROB, RANDOM_PROB)
    requests = request_generator.generate_requests(10000)

    print("\n---------------TEST---------------")

    # Service all memory access requests
    for mem_address in requests:
        caches[0].search_for_address(mem_address)

    # Print cache's in plain text
    for cache in caches:
        print(cache)
