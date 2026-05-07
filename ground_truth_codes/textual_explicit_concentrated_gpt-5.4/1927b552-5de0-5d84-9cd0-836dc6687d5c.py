import numpy as np
from scipy.stats import truncnorm

mu = 0.2
sigma = 0.15
a = 0.0
b = 0.5

# scipy's truncnorm uses standardized bounds
lower = (a - mu) / sigma
upper = (b - mu) / sigma

samples = []

for _ in range(10000):
    sample = truncnorm.rvs(lower, upper, loc=mu, scale=sigma)
    samples.append(float(sample))

print(samples)
