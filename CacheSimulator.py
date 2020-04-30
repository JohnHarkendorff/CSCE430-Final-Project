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
CACHE_BLOCK_SIZE = 2**5 				               # 32 bytes per block
L1_SIZES = [ ( 2 ** 14 ), ( 2 ** 15 ), ( 2 ** 16 ) ]   # 16k 32k 64k
L2_SIZES = [ ( 2 ** 15 ), ( 2 ** 16 ), ( 2 ** 17 ) ]   # 32k 64k 128k
L3_SIZES = [ ( 2 ** 16 ), ( 2 ** 17 ), ( 2 ** 18 ) ]   # 64k 128k 256k

# Cache access times, in nanoseconds
L1_ACCESS_TIMES = [ 0.35, 0.5, 0.805 ]
L2_ACCESS_TIMES = [ 0.5, 0.805, 1.1 ]
L3_ACCESS_TIMES = [ 0.805, 1.1, 1.416 ]
MAIN_MEM_ACCESS_TIME = 30

# Constants
MAX_ADDRESS_VALUE = 2**20 #simulate 20 bit address, 1MB of memory
MEM_REQUESTS = 10000

if __name__ == "__main__":

    # Have user select cache option
    print('\nOption 1:')
    print('Cache Levels: L1')

    print('\nOption 2:')
    print('Cache Levels: L1 and L2')

    print('\nOption 2:')
    print('Cache Levels: L1, L2, and L3')

    cache_size = int(input("Please enter if you want option 1, 2, or 3: "))

    print("---------------Running Simulation---------------")

    # Generate memory access requests
    request_generator = RequestGenerator(MAX_ADDRESS_VALUE, PREV_PROB, TEMPORAL_PROB, SPATIAL_PROB, RANDOM_PROB)
    requests = request_generator.generate_requests(MEM_REQUESTS)

    for i in range(0, len(L1_SIZES)):
        
        print("\n---------------TEST {}---------------".format(i+1))

        # Init selected cache option
        caches = []
        if cache_size == 1:
            caches.insert(0, Cache(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, None, MAIN_MEM_ACCESS_TIME, True))
            caches.insert(0, Cache(L1_SIZES[i], CACHE_BLOCK_SIZE, caches[0], L1_ACCESS_TIMES[i] ) )
        elif cache_size == 2:
            caches.insert(0, Cache(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, None, MAIN_MEM_ACCESS_TIME, True))
            caches.insert(0, Cache(L2_SIZES[i], CACHE_BLOCK_SIZE, caches[0], L2_ACCESS_TIMES[i] ) )
            caches.insert(0, Cache(L1_SIZES[i], CACHE_BLOCK_SIZE, caches[0], L1_ACCESS_TIMES[i] ) )
        elif cache_size == 3:
            caches.insert(0, Cache(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, None, MAIN_MEM_ACCESS_TIME, True))
            caches.insert(0, Cache(L3_SIZES[i], CACHE_BLOCK_SIZE, caches[0], L3_ACCESS_TIMES[i] ) )
            caches.insert(0, Cache(L2_SIZES[i], CACHE_BLOCK_SIZE, caches[0], L2_ACCESS_TIMES[i] ) )
            caches.insert(0, Cache(L1_SIZES[i], CACHE_BLOCK_SIZE, caches[0], L1_ACCESS_TIMES[i] ) )

        # Print results of init
        print("Number of caches: ", len(caches)-1) # minus 1 because memory is the last one
        print("L1 size (in bytes): {}, L1 access time (in ns): {}".format(caches[0].cache_size, caches[0].access_time) )
        if cache_size > 1:
            print("L2 size (in bytes): {}, L2 access time (in ns): {}".format(caches[1].cache_size, caches[1].access_time) )
        if cache_size > 2:
            print("L3 size (in bytes): {}, L3 access time (in ns): {}".format(caches[2].cache_size, caches[2].access_time) )
        print("Main mem size (in bytes): {}, Main mem access time (in ns): {}".format(caches[-1].cache_size, caches[-1].access_time) )      

        # Service all memory access requests
        for mem_address in requests:
            caches[0].search_for_address(mem_address)

        # Print cache's in plain text
        print("\nAfter running {} memory requests...".format(MEM_REQUESTS) )
        total_access_time = 0
        for cache in caches:
            print(cache)
            total_access_time += cache.access_time * cache.access_count
        print("Total access time (in ns): {}".format( total_access_time ) )
