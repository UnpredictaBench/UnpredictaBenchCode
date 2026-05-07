import numpy as np
from scipy.stats import poisson

lam = 18
samples = []

for _ in range(10000):
    sample = poisson.rvs(mu=lam)
    samples.append(sample)

print(samples)
