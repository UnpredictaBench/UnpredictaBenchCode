import numpy as np
from scipy.stats import gamma

alpha = 25
theta = 0.04
samples = []

for _ in range(10000):
    sample = gamma.rvs(a=alpha, scale=theta, size=1)[0]
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
