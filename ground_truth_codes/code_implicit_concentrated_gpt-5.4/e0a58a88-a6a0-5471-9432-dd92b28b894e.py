import numpy as np

rate_a = 0.7
rate_b = 0.4
samples = []

for _ in range(10000):
    arrivals_a = np.random.poisson(rate_a)
    arrivals_b = np.random.poisson(rate_b)
    sample = arrivals_a - arrivals_b
    samples.append(sample)

print(samples)
