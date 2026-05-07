import numpy as np

mu = 18.4
sigma = 9.7
samples = []

for _ in range(10000):
    sample = np.random.normal(loc=mu, scale=sigma)
    samples.append(sample)

print(samples)
