import numpy as np
from scipy.stats import laplace

mu = 12.5
b = 9.0
samples = []

for _ in range(10000):
    sample = laplace.rvs(loc=mu, scale=b)
    samples.append(float(sample))

print(samples)
