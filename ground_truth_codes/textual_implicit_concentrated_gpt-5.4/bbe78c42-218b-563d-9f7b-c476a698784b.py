import numpy as np
from scipy.stats import laplace

mu = 0.0
b = 0.2
samples = []

for _ in range(10000):
    sample = laplace.rvs(loc=mu, scale=b)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
