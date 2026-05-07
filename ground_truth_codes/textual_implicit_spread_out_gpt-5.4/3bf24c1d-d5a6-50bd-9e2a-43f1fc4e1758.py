import numpy as np
from scipy.stats import skellam

mu_1 = 18
mu_2 = 11
samples = []

for _ in range(10000):
    sample = skellam.rvs(mu_1, mu_2)
    samples.append(sample)

print(samples)
