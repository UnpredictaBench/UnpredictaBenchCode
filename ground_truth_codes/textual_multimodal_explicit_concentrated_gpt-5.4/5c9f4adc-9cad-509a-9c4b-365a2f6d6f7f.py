import numpy as np

weights = [0.5, 0.5]
ns = [3, 3]
ps = [0.2, 0.8]

samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    sample = np.random.binomial(ns[chosen], ps[chosen])
    samples.append(sample)

print(samples)
