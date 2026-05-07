import numpy as np
from scipy.stats import invgauss

mu = 1.0
lam = 40.0

samples = []
for _ in range(10000):
    sample = invgauss.rvs(mu=mu/lam, scale=lam)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
