import numpy as np
from scipy.stats import betabinom

n = 40
alpha = 1.2
beta = 1.1
samples = []

for _ in range(10000):
    sample = betabinom.rvs(n, alpha, beta)
    samples.append(sample)

print(samples)
