import numpy as np
from scipy.stats import beta

alpha = 0.6
beta_param = 0.7
samples = []

for _ in range(10000):
    sample = beta.rvs(alpha, beta_param)
    samples.append(float(sample))

print(samples)
