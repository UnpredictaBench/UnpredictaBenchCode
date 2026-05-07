import numpy as np

lam = 8.0
samples = []

for _ in range(10000):
    sample = np.random.exponential(scale=1/lam)
    samples.append(sample)

print(samples)
