import numpy as np
from scipy.stats import loguniform

a = 2.0
b = 2.5
samples = []

for _ in range(10000):
    sample = loguniform.rvs(a, b)
    samples.append(float(sample))

print(samples)
