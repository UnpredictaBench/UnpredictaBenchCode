import numpy as np
from scipy.stats import chi2

k = 61
samples = []

for _ in range(10000):
    sample = chi2.rvs(df=k)
    samples.append(float(sample))

print(samples)
