import numpy as np
from scipy.stats import lognorm

mu = 0.0
sigma = 0.2
samples = []

for _ in range(10000):
    sample = lognorm(s=sigma, scale=np.exp(mu)).rvs()
    samples.append(float(sample))  # Convert to float for a valid Python list

print(samples)
