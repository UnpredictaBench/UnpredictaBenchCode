import numpy as np
from scipy.stats import weibull_min

k = 8.0
lambda_ = 1.2
samples = []

for _ in range(10000):
    sample = weibull_min.rvs(c=k, scale=lambda_)
    samples.append(float(sample))

print(samples)
