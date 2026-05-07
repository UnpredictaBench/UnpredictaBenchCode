import numpy as np

samples = []
weights = np.array([80.0, 85.0, 90.0, 95.0])

for _ in range(10000):
    rng = np.random.default_rng()
    raw = rng.gamma(shape=weights, scale=1.0)
    parts = raw / raw.sum()
    outcome = parts[2]
    samples.append(float(outcome))

print(samples)
