import numpy as np

samples = []
rng = np.random.default_rng()

for _ in range(10000):
    z = rng.normal(loc=0.0, scale=1.0)
    samples.append(z)

print(samples)
