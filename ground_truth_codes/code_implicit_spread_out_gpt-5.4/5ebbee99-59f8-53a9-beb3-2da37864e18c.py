import numpy as np

rng = np.random.default_rng()

mean = np.array([0.0, 12.0, -8.0])
cov = np.array([
    [25.0, 10.0, -6.0],
    [10.0, 16.0,  5.0],
    [-6.0,  5.0,  9.0]
])

values = []

for _ in range(10000):
    sample = rng.multivariate_normal(mean, cov)
    values.append(sample[0])

print(values)