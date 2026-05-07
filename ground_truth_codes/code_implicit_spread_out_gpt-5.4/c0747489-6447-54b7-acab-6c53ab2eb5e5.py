import random
import math

a = -120.0
b = 180.0
c = 35.0
threshold = (c - a) / (b - a)
samples = []

for _ in range(10000):
    u = random.random()
    if u < threshold:
        x = a + math.sqrt(u * (b - a) * (c - a))
    else:
        x = b - math.sqrt((1 - u) * (b - a) * (b - c))
    samples.append(x)

print(samples)
