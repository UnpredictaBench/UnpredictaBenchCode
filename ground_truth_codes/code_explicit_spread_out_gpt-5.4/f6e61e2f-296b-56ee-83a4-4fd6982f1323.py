import numpy as np

# Laplace distribution parameters
mu = -3.5
b = 12.0

samples = []

for _ in range(10000):
    sample = np.random.laplace(loc=mu, scale=b)
    samples.append(sample)

print(samples)
