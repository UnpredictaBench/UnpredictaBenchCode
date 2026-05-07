import numpy as np

a = 0.2
b = 0.6
samples = []

for _ in range(10000):
    sample = np.random.uniform(a, b)
    samples.append(sample)

print(samples)
