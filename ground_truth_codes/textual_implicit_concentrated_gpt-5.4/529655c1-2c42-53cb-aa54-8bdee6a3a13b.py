import numpy as np
from scipy.stats import nbinom

r = 4
p = 0.92
samples = []

for _ in range(10000):
    sample = nbinom.rvs(r, p)
    samples.append(sample)

print(samples)
