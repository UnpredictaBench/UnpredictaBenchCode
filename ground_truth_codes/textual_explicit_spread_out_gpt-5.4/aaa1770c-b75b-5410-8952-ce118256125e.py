import numpy as np

a = -250
b = 750
samples = []

for _ in range(10000):
    sample = np.random.uniform(low=a, high=b)
    samples.append(sample)

print(samples)
