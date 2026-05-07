import numpy as np

samples = []
rng = np.random.default_rng()

for _ in range(10000):
    z = rng.standard_normal()
    samples.append(float(z**2))

print(samples)
