import numpy as np

# Hypergeometric distribution parameters
N = 40   # population size
K = 4    # number of success states in the population
n = 3    # number of draws without replacement

samples = []

for _ in range(10000):
    sample = np.random.hypergeometric(ngood=K, nbad=N-K, nsample=n)
    samples.append(sample)

print(samples)
