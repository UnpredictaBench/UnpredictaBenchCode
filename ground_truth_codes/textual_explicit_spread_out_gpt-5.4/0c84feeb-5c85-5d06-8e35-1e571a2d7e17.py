import numpy as np
from scipy.stats import lognorm

mu = 1.2
sigma = 2.4
samples = []

for _ in range(10000):
    sample = lognorm(s=sigma, scale=np.exp(mu)).rvs()
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
