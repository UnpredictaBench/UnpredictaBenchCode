import numpy as np

stages = 7
rate = 0.35
samples = []

for _ in range(10000):
    u = np.random.uniform(size=stages)
    sample = -np.log(np.prod(u)) / rate
    samples.append(float(sample))

print(samples)
