import numpy as np
from scipy.stats import truncnorm

# Parameters for a truncated normal distribution
mu = 0.0
sigma = 8.0
a = -20.0
b = 20.0

# SciPy parameterization uses standardized bounds
lower = (a - mu) / sigma
upper = (b - mu) / sigma

# List to store samples
samples = []

# Draw samples in a loop
for _ in range(10000):
    sample = truncnorm.rvs(lower, upper, loc=mu, scale=sigma)
    samples.append(float(sample))

# Print the final list of samples
print(samples)
