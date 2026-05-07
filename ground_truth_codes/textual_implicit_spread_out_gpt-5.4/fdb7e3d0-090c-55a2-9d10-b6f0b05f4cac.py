import numpy as np
from scipy.stats import truncnorm

mu = 15
sigma = 12
a = -40
b = 55

alpha = (a - mu) / sigma
beta = (b - mu) / sigma

samples = []
for _ in range(10000):
    sample = truncnorm.rvs(alpha, beta, loc=mu, scale=sigma)
    samples.append(float(sample))  # Convert np.float64 to Python float

print(samples)
