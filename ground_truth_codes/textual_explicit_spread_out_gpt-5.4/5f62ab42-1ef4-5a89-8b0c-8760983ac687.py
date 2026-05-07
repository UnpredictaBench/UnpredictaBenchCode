import numpy as np
from scipy.stats import logistic

mu = -12.5
s = 9.0
samples = []

for _ in range(10000):
    sample = logistic.rvs(loc=mu, scale=s)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
