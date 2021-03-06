import random

# Generates random requests to send to the cache class				
class RequestGenerator:
    def __init__(self, max_value, prev_prob, temp_prob, spatial_prob, rand_prob):
        self.requests = []
        self.max_value = max_value

        self.prev_prob = prev_prob
        self.temp_prob = temp_prob
        self.spatial_prob = spatial_prob
        self.rand_prob = rand_prob

    def generate_requests(self, num_requests, ):
        for i in range(num_requests):
            ran_num = random.random()
            
            # Chance of using the previous request
            if ran_num <= self.prev_prob:
                self.requests.append(self.prev_value())
            # Chance of using any of the past 5 requests
            elif ran_num <= (self.prev_prob + self.temp_prob):
                self.requests.append(self.temporal())
            # Chance of using a value close to the previous request's value
            elif ran_num <= (self.prev_prob + self.temp_prob + self.spatial_prob):
                self.requests.append(self.spatial())
            # Chance of a completely random value
            elif ran_num <= (self.prev_prob + self.temp_prob + self.spatial_prob + self.rand_prob):
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