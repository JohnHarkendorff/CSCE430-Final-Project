#!/usr/bin/env python
import random
import sys

from Cache import Cache
from Cache import CacheBlock
from RequestGenerator import RequestGenerator

# Probabilities of different types of access
PREV_PROB = 0.1
TEMPORAL_PROB = 0.30
SPATIAL_PROB = 0.30
RANDOM_PROB = 1.0 - PREV_PROB - TEMPORAL_PROB - SPATIAL_PROB

# Cache sizes, all need to be multiples of CACHE_BLOCK_SIZE
CACHE_BLOCK_SIZE = 2**4 				# 16 bytes per block
L1_SIZE = CACHE_BLOCK_SIZE * ( 2 ** 5 ) # 32 blocks in L1
L2_SIZE = CACHE_BLOCK_SIZE * ( 2 ** 7 ) # 128 blocks in L2
L3_SIZE = CACHE_BLOCK_SIZE * ( 2 ** 9 ) # 512 blocks in L3

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
        caches.append(Cache(L1_SIZE, CACHE_BLOCK_SIZE))
        caches.append(Cache(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, True))
    elif cache_size == 2:
        caches.append(Cache(L1_SIZE, CACHE_BLOCK_SIZE))
        caches.append(Cache(L2_SIZE, CACHE_BLOCK_SIZE))
        caches.append(Cache(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, True))
    elif cache_size == 3:
        caches.append(Cache(L1_SIZE, CACHE_BLOCK_SIZE))
        caches.append(Cache(L2_SIZE, CACHE_BLOCK_SIZE))
        caches.append(Cache(L3_SIZE, CACHE_BLOCK_SIZE))
        caches.append(Cache(MAX_ADDRESS_VALUE, CACHE_BLOCK_SIZE, True))

    print("Number of caches: ", len(caches)-1) # minus 1 because memory is the last one
    print("L1 length: ", len(caches[0].cache_blocks))
    print("Main mem length: ", len(caches[len(caches) - 1].cache_blocks))

    request_generator = RequestGenerator(MAX_ADDRESS_VALUE)
    requests = request_generator.generate_requests(1000)
