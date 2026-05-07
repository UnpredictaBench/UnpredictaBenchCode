import numpy as np
from scipy.stats import nbinom

r = 17
p = 0.23
samples = []

for _ in range(10000):
    sample = int(nbinom.rvs(r, p, size=1)[0])
    samples.append(sample)

print(samples)
