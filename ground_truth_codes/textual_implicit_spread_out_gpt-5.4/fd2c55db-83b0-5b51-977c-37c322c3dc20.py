import numpy as np
from scipy.stats import weibull_min

lam = 18.7
k = 0.62
samples = []

for _ in range(10000):
    sample = weibull_min.rvs(c=k, scale=lam)
    samples.append(float(sample))  # Convert to float to ensure valid Python literal

print(samples)
