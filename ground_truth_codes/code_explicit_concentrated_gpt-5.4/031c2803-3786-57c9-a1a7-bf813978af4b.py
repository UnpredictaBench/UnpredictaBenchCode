import numpy as np

a = 0.2
b = 0.5
samples = []

for _ in range(10000):
    sample = np.random.uniform(low=a, high=b)
    samples.append(sample)

print(samples)
