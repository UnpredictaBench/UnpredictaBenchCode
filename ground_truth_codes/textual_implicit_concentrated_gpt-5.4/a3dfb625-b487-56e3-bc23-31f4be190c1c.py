import numpy as np
from scipy.stats import geom

p = 0.85
samples = []

for _ in range(10000):
    sample = geom.rvs(p)
    samples.append(sample)

print(samples)
