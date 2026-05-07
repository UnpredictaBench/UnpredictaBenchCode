import numpy as np

p = np.array([0.08, 0.12, 0.10, 0.15])
rng = np.random.default_rng()
samples = []

for _ in range(10000):
    sample = rng.binomial(1, p).sum()
    samples.append(int(sample))

print(samples)
