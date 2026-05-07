import numpy as np

a = -120.5
b = 340.75
samples = []

for _ in range(10000):
    sample = np.random.uniform(a, b)
    samples.append(sample)

print(samples)
