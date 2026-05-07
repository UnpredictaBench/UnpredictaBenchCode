import numpy as np
from scipy.stats import beta

alpha = 1.0
beta_param = 0.5
samples = []

for _ in range(10000):
    sample = beta.rvs(alpha, beta_param)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
