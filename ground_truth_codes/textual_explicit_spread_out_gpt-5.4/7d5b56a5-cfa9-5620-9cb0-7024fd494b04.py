import numpy as np
from scipy.stats import hypergeom

N = 120
K = 55
n = 60

samples = []

for _ in range(10000):
    sample = hypergeom.rvs(M=N, n=K, N=n)
    samples.append(sample)

print(samples)
