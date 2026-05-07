import numpy as np
from scipy.stats import beta

alpha = 48
beta_param = 52
samples = []

for _ in range(10000):
    sample = beta.rvs(alpha, beta_param)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
