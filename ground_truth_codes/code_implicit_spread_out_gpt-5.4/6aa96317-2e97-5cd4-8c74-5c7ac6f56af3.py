import numpy as np

samples = []
weights = np.array([0.12, 0.18, 0.09, 0.16, 0.11, 0.14, 0.08, 0.12], dtype=float)

for _ in range(10000):
    rng = np.random.default_rng()
    parts = rng.gamma(shape=weights, scale=1.0)
    share = parts / parts.sum()
    samples.append(float(share[0]))

print(samples)
