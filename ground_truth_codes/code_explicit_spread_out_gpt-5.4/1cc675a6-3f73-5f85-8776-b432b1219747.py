import numpy as np

# Skellam sampling via the difference of two independent Poisson variables
mu1 = 28.0
mu2 = 19.0
samples = []

for _ in range(10000):
    n1 = np.random.poisson(lam=mu1)
    n2 = np.random.poisson(lam=mu2)
    sample = n1 - n2
    samples.append(sample)

print(samples)
