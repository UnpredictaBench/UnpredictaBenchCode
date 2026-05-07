import numpy as np
from scipy.stats import pareto

x_m = 0.8
alpha = 0.55
samples = []

for _ in range(10000):
    sample = pareto.rvs(b=alpha, scale=x_m)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
