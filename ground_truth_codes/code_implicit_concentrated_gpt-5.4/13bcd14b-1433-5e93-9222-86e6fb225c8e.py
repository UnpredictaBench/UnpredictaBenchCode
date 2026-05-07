import numpy as np

trials = 6
chance = 0.18
samples = []

for _ in range(10000):
    sample = np.random.default_rng().binomial(n=trials, p=chance)
    samples.append(sample)

print(samples)
