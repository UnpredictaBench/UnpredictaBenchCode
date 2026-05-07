import numpy as np
from scipy.stats import skellam

mu_1 = 0.8
mu_2 = 0.5
samples = []

for _ in range(10000):
    sample = skellam.rvs(mu_1, mu_2)
    samples.append(int(sample))

print(samples)
