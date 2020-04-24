#!/usr/bin/env python
import random
import sys

# Probabilities of different types of access
PREV_PROB = 0.1
TEMPORAL_PROB = 0.30
SPATIAL_PROB = 0.30
RANDOM_PROB = 1.0 - PREV_PROB - TEMPORAL_PROB - SPATIAL_PROB
L1_SIZE = 2**5
L2_SIZE = 2**6
L3_SIZE = 2**7

# Constants to be input later
MAX_ADDRESS_VALUE = 2**16 #simulate 16 bit address

class Cache:
	def __init__(self, cache_size, main_mem_flag):
		self.cache_size = cache_size
		self.cache_blocks = []
		if main_mem_flag:
			for i in range(self.cache_size):
				self.cache_blocks.append(Cache_Block(i))
					
class Cache_Block:
	def __init__(self, data_value):	
		# This will be a number between 0 and the size of the cache. The value can only occur once for each cache level
		self.last_used = 0
		self.data_value = data_value
				
# Generates random requests to send to the cache class				
class Request_Generator:
	def __init__(self, max_value):
		self.requests = []
		self.max_value = max_value

	def generate_requests(self, num_requests):
		for i in range(num_requests):
			ran_num = random.random()
			
			# Chance of using the previous request
			if ran_num <= PREV_PROB:
				self.requests.append(self.prev_value())
			# Chance of using any of the past 5 requests
			elif ran_num <= (PREV_PROB + TEMPORAL_PROB):
				self.requests.append(self.temporal())
			# Chance of using a value close to the previous request's value
			elif ran_num <= (PREV_PROB + TEMPORAL_PROB + SPATIAL_PROB):
				self.requests.append(self.spatial())
			# Chance of a completely random value
			elif ran_num <= (PREV_PROB + TEMPORAL_PROB + SPATIAL_PROB + RANDOM_PROB):
				self.requests.append(self.random_value())
		
		return self.requests
			
	# Use same address as before
	def prev_value(self):
		if len(self.requests) == 0:
			return self.random_value()
			
		return self.requests[len(self.requests) - 1]
	
	# Use a recently used value
	def temporal(self):
		if len(self.requests) < 5:
			return self.random_value()
			
		ran_num = random.randint(1, 5)
		return self.requests[len(self.requests) - ran_num]
	
	# Use a nearby value
	def spatial(self):
		if len(self.requests) == 0:
			return self.random_value()
			
		ran_num = random.randint(-8, 8)
		appended_value = self.requests[len(self.requests) - 1] + ran_num
		if appended_value > self.max_value:
			appended_value = self.max_value
		elif appended_value < 0:
			appended_value = 0
		
		return appended_value
	
	# Use a random value
	def random_value(self):
		return random.randint(0, self.max_value)
		
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
		caches.append(Cache(L1_SIZE, False))
		caches.append(Cache(MAX_ADDRESS_VALUE, True))
	elif cache_size == 2:
		caches.append(Cache(L1_SIZE, False))
		caches.append(Cache(L2_SIZE, False))
		caches.append(Cache(MAX_ADDRESS_VALUE, True))
	elif cache_size == 3:
		caches.append(Cache(L1_SIZE, False))
		caches.append(Cache(L2_SIZE, False))
		caches.append(Cache(L3_SIZE, False))
		caches.append(Cache(MAX_ADDRESS_VALUE, True))
	
	print("Number of caches: ", len(caches))
	print("L1 length: ", len(caches[0].cache_blocks))
	print("Main mem length: ", len(caches[len(caches) - 1].cache_blocks))
	
	request_generator = Request_Generator(MAX_ADDRESS_VALUE)
	requests = request_generator.generate_requests(1000)
