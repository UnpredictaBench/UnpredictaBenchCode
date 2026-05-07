import numpy as np
from scipy.stats import betabinom

n = 4
alpha = 20
beta = 20
samples = []

for _ in range(10000):
    sample = betabinom.rvs(n, alpha, beta)
    samples.append(int(sample))

print(samples)
