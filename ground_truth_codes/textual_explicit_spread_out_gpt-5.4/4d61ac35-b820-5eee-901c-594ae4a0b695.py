import numpy as np
from scipy.stats import skellam

mu1 = 18.7
mu2 = 14.2
samples = []

for _ in range(10000):
    sample = skellam.rvs(mu1, mu2)
    samples.append(int(sample))

print(samples)
