import numpy as np
from scipy.stats import weibull_min

lambda_ = 0.9
k = 4.0
samples = []

for _ in range(10000):
    sample = weibull_min.rvs(c=k, scale=lambda_)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
