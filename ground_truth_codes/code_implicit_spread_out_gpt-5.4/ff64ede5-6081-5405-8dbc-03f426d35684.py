import math
import random

rate = 18.7
samples = []

for _ in range(10000):
    threshold = math.exp(-rate)
    count = 0
    product = 1.0

    while product > threshold:
        count += 1
        product *= random.random()

    sample = count - 1
    samples.append(sample)

print(samples)
