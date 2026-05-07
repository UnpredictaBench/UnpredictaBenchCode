import numpy as np
from scipy.stats import gamma

alpha = 0.7
theta = 9.5
samples = []

for _ in range(10000):
    sample = gamma.rvs(a=alpha, scale=theta, size=1)[0]
    samples.append(float(sample))

print(samples)
