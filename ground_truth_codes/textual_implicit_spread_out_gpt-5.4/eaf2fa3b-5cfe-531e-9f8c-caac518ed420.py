import numpy as np
from scipy.stats import poisson, gamma

lam = 12.4
shape = 2.3
rate = 0.18
scale = 1 / rate

samples = []

for _ in range(10000):
    N = poisson.rvs(mu=lam)
    if N == 0:
        sample = 0.0
    else:
        sample = gamma.rvs(a=shape, scale=scale, size=N).sum()
    samples.append(float(sample))

print(samples)
