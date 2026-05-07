import numpy as np
from scipy.stats import gamma

alpha = 2.4
theta = 9.5
samples = []

for _ in range(10000):
    sample = float(gamma.rvs(a=alpha, scale=theta, size=1)[0])
    samples.append(sample)

print(samples)
