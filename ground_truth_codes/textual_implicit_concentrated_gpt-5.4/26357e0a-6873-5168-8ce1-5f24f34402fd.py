import numpy as np

mu = -0.15
sigma = 0.08
samples = []

for _ in range(10000):
    s = np.random.normal(loc=mu, scale=sigma)
    sample = max(0.0, s)
    samples.append(sample)

print(samples)
