import numpy as np

rng = np.random.default_rng()
weights = np.array([0.88, 0.07, 0.03, 0.02], dtype=float)
cutoffs = np.cumsum(weights)

samples = []
for _ in range(10000):
    u = rng.random()
    sample = int(np.searchsorted(cutoffs, u) + 1)
    samples.append(sample)

print(samples)
