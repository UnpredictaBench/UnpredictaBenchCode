import numpy as np

stages = 3
rate = 4.5
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0, size=stages)
    sample = -np.sum(np.log(u)) / rate
    samples.append(float(sample))

print(samples)
