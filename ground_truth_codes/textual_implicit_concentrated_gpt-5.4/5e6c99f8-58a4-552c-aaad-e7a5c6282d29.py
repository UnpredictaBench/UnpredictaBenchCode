import numpy as np
from scipy.stats import pareto

x_m = 1000
alpha = 8

samples = []

for _ in range(10000):
    sample = pareto.rvs(b=alpha, scale=x_m, size=1)[0]
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
