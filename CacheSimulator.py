#!/usr/bin/env python

class Cache:
	# cache_levls: int, the number of cache levels
	# cache_blocks: array<int>, the number of cache blocks per level
	def __init__(self, cache_levels, cache_blocks):
		if cache_levels != len(cache_blocks):
			return False
			
		self.cache_levels = cache_levels
		self.cache_values = []
		for i in range(0, cache_levels):
			cache_block = []
			for j in range(0, cache_blocks[i]):
				cache_block.append(-1)
				
			self.cache_values.append(cache_block)
			
		
		
	def get_data(self, data_address):
		data = -1
		for i in range(0, cache_values):
			for j in range(0, cache_values[i]):
				if 
		
		
if __name__ == "__main__":
	TODO()
	
def TODO():
	print "gotta do this"