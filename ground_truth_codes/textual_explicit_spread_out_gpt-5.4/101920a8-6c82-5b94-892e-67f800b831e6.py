import numpy as np
from scipy.stats import gumbel_r

mu = 12.5
beta = 9.0
samples = []

for _ in range(10000):
    sample = gumbel_r.rvs(loc=mu, scale=beta)
    samples.append(float(sample))  # Convert np.float64 to float for a valid Python literal

print(samples)
