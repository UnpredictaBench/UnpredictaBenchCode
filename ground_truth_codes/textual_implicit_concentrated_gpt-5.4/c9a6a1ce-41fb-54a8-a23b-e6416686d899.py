import numpy as np

a = 2.1
b = 2.8
samples = []

for _ in range(10000):
    sample = np.random.uniform(a, b)
    samples.append(sample)

print(samples)
