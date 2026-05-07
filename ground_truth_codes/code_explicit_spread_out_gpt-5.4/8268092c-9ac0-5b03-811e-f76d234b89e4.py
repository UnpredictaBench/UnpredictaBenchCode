import numpy as np

a = -1000.0
b = 1000.0
samples = []

for _ in range(10000):
    sample = np.random.uniform(low=a, high=b)
    samples.append(sample)

print(samples)
