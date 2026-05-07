import numpy as np

mu = 0.0
b = 0.25
samples = []

for _ in range(10000):
    sample = np.random.laplace(loc=mu, scale=b)
    samples.append(sample)

print(samples)
