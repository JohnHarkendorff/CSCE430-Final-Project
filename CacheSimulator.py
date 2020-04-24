#!/usr/bin/env python
import random

# Probabilities of different types of access
PREV_PROB = 0.1
TEMPORAL_PROB = 0.30
SPATIAL_PROB = 0.30
RANDOM_PROB = 1.0 - PREV_PROB - TEMPORAL_PROB - SPATIAL_PROB

class Cache:
	def __init__(self):
		return null

# Generates random requests to send to the cache class				
class Request_Generator:
	def __init__(self):
		self.requests = []
		self.max_value = 10000

	def generate_requests(self, num_requests):
		for i in range(num_requests):
			ran_num = random.random()
			
			# Chance of using the previous request
			if ran_num <= PREV_PROB:
				self.requests.append(self.prev_value())
			# Chance of using any of the past 5 requests
			elif ran_num <= (PREV_PROB + TEMPORAL_PROB):
				self.requests.append(self.past_five())
			# Chance of using a value close to the previous request's value
			elif ran_num <= (PREV_PROB + TEMPORAL_PROB + SPATIAL_PROB):
				self.requests.append(self.temporal())
			# Chance of a completely random value
			elif ran_num <= (PREV_PROB + TEMPORAL_PROB + SPATIAL_PROB + RANDOM_PROB):
				self.requests.append(self.random_value())
		
		return self.requests
			
	def prev_value(self):
		if len(self.requests) == 0:
			return self.random_value()
			
		return self.requests[len(self.requests) - 1]
		
	def past_five(self):
		if len(self.requests) < 5:
			return self.random_value()
			
		ran_num = random.randint(1, 5)
		return self.requests[len(self.requests) - ran_num]
		
	def temporal(self):
		if len(self.requests) == 0:
			return self.random_value()
			
		ran_num = random.randint(-8, 8)
		appended_value = self.requests[len(self.requests) - 1] + ran_num
		if appended_value > self.max_value:
			appended_value = self.max_value
		elif appended_value < 0:
			appended_value = 0
		
		return appended_value
		
	def random_value(self):
		return random.randint(0, self.max_value)
		
if __name__ == "__main__":
	request_generator = Request_Generator()
	requests = request_generator.generate_requests(1000)
	print(requests)
