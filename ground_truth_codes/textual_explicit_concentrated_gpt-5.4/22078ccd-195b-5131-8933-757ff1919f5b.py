import numpy as np
from scipy.stats import nbinom

r = 4
p = 0.85

samples = []
for _ in range(10000):
    sample = nbinom.rvs(r, p)
    samples.append(int(sample))

print(samples)
