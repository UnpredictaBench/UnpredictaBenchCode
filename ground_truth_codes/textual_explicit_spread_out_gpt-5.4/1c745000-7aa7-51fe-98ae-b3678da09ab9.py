import numpy as np
from scipy.stats import weibull_min

lam = 12.5
k = 0.65
samples = []

for _ in range(10000):
    sample = weibull_min.rvs(c=k, scale=lam)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
