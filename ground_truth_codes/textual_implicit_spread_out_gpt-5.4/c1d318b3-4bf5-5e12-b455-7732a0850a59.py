import numpy as np
from scipy.stats import gumbel_r

mu = 18.5
beta = 6.8
samples = []

for _ in range(10000):
    sample = gumbel_r.rvs(loc=mu, scale=beta)
    samples.append(float(sample))

print(samples)
