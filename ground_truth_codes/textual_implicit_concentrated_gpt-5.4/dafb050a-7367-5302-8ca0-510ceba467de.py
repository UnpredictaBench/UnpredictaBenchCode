import numpy as np
from scipy.stats import gumbel_r

mu = 0.2
beta = 0.15
samples = []

for _ in range(10000):
    sample = gumbel_r.rvs(loc=mu, scale=beta)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
