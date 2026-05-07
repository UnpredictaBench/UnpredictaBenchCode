import numpy as np
from scipy.stats import betabinom

n = 6
alpha = 18
beta = 42
samples = []

for _ in range(10000):
    sample = betabinom.rvs(n, alpha, beta)
    samples.append(sample)

print(samples)
