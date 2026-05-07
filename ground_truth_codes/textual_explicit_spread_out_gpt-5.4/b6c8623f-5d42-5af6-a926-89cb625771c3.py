import numpy as np
from scipy.stats import truncnorm

mu = 0
sigma = 12
a = -30
b = 30

lower = (a - mu) / sigma
upper = (b - mu) / sigma

samples = []
for _ in range(10000):
    sample = truncnorm.rvs(lower, upper, loc=mu, scale=sigma)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
