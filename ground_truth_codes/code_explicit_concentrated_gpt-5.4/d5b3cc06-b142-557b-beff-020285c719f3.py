import numpy as np

# Skellam sampling via difference of two independent Poisson variables
mu1 = 0.8
mu2 = 0.5

samples = []

for _ in range(10000):
    n1 = np.random.poisson(lam=mu1)
    n2 = np.random.poisson(lam=mu2)
    sample = n1 - n2
    samples.append(sample)

print(samples)
