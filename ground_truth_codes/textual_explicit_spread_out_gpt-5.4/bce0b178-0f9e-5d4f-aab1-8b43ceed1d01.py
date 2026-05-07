import numpy as np
from scipy.stats import dirichlet

alpha = np.array([0.18, 0.27, 0.22, 0.13])
samples = []

for _ in range(10000):
    sample = dirichlet.rvs(alpha, size=1)[0]
    samples.append(float(sample[0]))  # Convert to float before appending

print(samples)
