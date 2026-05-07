import numpy as np
from scipy.stats import dirichlet

alpha = np.array([120, 150, 130, 140], dtype=float)
samples = []

for _ in range(10000):
    sample = dirichlet.rvs(alpha, size=1)[0]
    samples.append(float(sample[1]))  # Convert to float

print(samples)
