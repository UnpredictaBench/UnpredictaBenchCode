import numpy as np

mu = 25.0
sigma = 12.0
samples = []

for _ in range(10000):
    sample = np.random.normal(loc=mu, scale=sigma)
    samples.append(sample)

print(samples)
