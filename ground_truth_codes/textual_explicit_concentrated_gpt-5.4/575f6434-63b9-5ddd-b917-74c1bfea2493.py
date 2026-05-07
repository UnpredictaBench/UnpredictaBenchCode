import numpy as np
from scipy.stats import pareto

x_m = 5
alpha = 25
samples = []

for _ in range(10000):
    sample = pareto.rvs(b=alpha, scale=x_m)
    samples.append(float(sample))

print(samples)
