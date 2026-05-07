import numpy as np

# Rectified Gaussian parameters
mu = -0.2
sigma = 0.15

samples = []

for _ in range(10000):
    s = np.random.normal(loc=mu, scale=sigma)
    sample = max(0, s)
    samples.append(sample)

print(samples)
