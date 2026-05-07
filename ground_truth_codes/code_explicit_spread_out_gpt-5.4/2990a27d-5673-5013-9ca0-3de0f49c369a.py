import numpy as np

# Rectified Gaussian: X = max(0, S) where S ~ Normal(mu, sigma^2)
mu = 8.0
sigma = 12.0

samples = []

for _ in range(10000):
    s = np.random.normal(loc=mu, scale=sigma)
    sample = max(0, s)
    samples.append(sample)

print(samples)
