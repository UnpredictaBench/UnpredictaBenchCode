import numpy as np
from scipy.stats import norm

mu = 0
sigma = 10
samples = []

for _ in range(10000):
    sample = norm.rvs(loc=mu, scale=sigma)
    samples.append(float(sample))

print(samples)
