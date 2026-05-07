import numpy as np

# Rayleigh mixture distribution sampler via hierarchical sampling
# First sample the mixing variable r from a Rayleigh distribution,
# then sample x from a conditional density tau(x, r; n).
# Here we choose tau(x, r; n) to be a Normal distribution with mean r
# and standard deviation 1/n, which is a valid probability density.

sigma = 0.35
n = 12.0

samples = []

for _ in range(10000):
    r = np.random.rayleigh(scale=sigma)
    x = np.random.normal(loc=r, scale=1.0 / n)
    samples.append(x)

print(samples)
