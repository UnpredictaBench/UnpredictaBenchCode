import numpy as np
from scipy.stats import gamma

alpha = 6
theta = 0.4
samples = []

for _ in range(10000):
    sample = gamma.rvs(a=alpha, scale=theta)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
