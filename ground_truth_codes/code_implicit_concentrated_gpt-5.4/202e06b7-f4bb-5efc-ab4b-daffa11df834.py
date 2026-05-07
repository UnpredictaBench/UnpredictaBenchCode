import numpy as np

rng = np.random.default_rng()
center = np.array([0.08, -0.04, 0.03])
shape = np.array([
    [0.05, 0.01, 0.0],
    [0.01, 0.04, 0.005],
    [0.0, 0.005, 0.03]
])
L = np.linalg.cholesky(shape)

samples = []
for _ in range(10000):
    base = rng.standard_normal(3)
    point = center + L @ base
    sample = float(point[0] + 0.5 * point[1] - 0.25 * point[2])
    samples.append(sample)

print(samples)
