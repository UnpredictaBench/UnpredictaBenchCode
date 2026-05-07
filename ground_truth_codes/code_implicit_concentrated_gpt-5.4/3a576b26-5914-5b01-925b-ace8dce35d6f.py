import math
import random

rate = 0.8
threshold = math.exp(-rate)
samples = []

for _ in range(10000):
    count = 0
    product = 1.0
    while product > threshold:
        product *= random.random()
        count += 1
    sample = count - 1
    samples.append(sample)

print(samples)
