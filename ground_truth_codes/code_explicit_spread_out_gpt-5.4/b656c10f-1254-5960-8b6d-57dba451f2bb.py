import numpy as np

# Hypergeometric sampling: successes drawn without replacement
# Parameters:
# N = population size
# K = number of success states in the population
# n = number of draws
N = 200
K = 100
n = 100

samples = []

for _ in range(10000):
    sample = np.random.hypergeometric(ngood=K, nbad=N-K, nsample=n)
    samples.append(sample)

print(samples)
