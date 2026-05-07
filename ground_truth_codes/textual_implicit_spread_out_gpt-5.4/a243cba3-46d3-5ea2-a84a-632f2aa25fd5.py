import numpy as np
from scipy.stats import nbinom

r = 9
p = 0.22
samples = []

for _ in range(10000):
    sample = nbinom.rvs(r, p)
    samples.append(sample)

print(samples)
