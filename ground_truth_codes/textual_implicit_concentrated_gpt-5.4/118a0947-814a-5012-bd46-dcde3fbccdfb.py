import numpy as np

mu = 0.0
sigma = 0.2
samples = []

for _ in range(10000):
    sample = np.random.normal(loc=mu, scale=sigma)
    samples.append(sample)

print(samples)
