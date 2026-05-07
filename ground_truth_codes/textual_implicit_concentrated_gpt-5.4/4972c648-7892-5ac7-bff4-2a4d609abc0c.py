import numpy as np
from scipy.stats import truncnorm

mu = 0.05
sigma = 0.12
a = -0.4
b = 0.4

alpha = (a - mu) / sigma
beta = (b - mu) / sigma

samples = []
for _ in range(10000):
    sample = truncnorm.rvs(alpha, beta, loc=mu, scale=sigma)
    samples.append(float(sample))

print(samples)
