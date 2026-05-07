import numpy as np
from scipy.stats import invgauss

mu = 9.5
lam = 0.8
samples = []

for _ in range(10000):
    sample = invgauss.rvs(mu / lam, scale=lam)
    samples.append(float(sample))  # Convert np.float64 to Python float

print(samples)
