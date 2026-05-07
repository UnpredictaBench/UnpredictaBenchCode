import numpy as np
from scipy.stats import invgauss

mu = 12.0
lam = 1.5
samples = []

for _ in range(10000):
    sample = invgauss.rvs(mu / lam, scale=lam)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
