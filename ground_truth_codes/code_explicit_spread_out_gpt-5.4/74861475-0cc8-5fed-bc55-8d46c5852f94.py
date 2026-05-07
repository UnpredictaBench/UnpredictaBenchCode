import numpy as np

mu = 0.8
sigma = 1.9

samples = []

for _ in range(10000):
    sample = np.random.lognormal(mean=mu, sigma=sigma)
    samples.append(sample)

print(samples)
