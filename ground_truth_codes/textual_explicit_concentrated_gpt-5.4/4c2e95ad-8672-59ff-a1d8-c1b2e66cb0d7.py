import numpy as np
from scipy.stats import hypergeom

N = 18  # population size
K = 3   # number of success states in the population
n = 5   # number of draws

samples = []

for _ in range(10000):
    sample = hypergeom.rvs(M=N, n=K, N=n)
    samples.append(int(sample))

print(samples)
