import numpy as np
from scipy.stats import geom

p = 0.08
samples = []

for _ in range(10000):
    trials_until_success = geom.rvs(p)
    sample = trials_until_success - 1
    samples.append(sample)

print(samples)
