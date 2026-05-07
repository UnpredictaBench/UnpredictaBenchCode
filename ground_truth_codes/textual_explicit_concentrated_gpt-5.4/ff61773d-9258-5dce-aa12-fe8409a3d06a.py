import numpy as np
from scipy.stats import laplace

mu = 0.2
b = 0.15
samples = []

for _ in range(10000):
    sample = laplace.rvs(loc=mu, scale=b)
    samples.append(float(sample))

print(samples)
