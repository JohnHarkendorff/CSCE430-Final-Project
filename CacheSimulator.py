#!/usr/bin/env python
import random

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
			
			# 10% chance of using the previous request
			if ran_num < 0.1:
				self.requests.append(self.prev_value())
			# 10% chance of using any of the past 5 requests
			elif ran_num < 0.2:
				self.requests.append(self.past_five())
			# 10% chance of using a value close to the previous request's value
			elif ran_num < 0.3:
				self.requests.append(self.temporal())
			# 70% chance of a completely random value
			else:
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
	requests = request_generator.generate_requests(10000)
	print(requests)
