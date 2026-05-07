import numpy as np
from scipy.stats import skellam

mu1 = 0.8
mu2 = 0.3
samples = []

for _ in range(10000):
    sample = skellam.rvs(mu1, mu2)
    samples.append(int(sample))

print(samples)
