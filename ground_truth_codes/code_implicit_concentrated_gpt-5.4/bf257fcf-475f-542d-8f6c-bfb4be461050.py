import numpy as np

shape = 18.0
scale = 0.12
samples = []

rng = np.random.default_rng()

for _ in range(10000):
    sample = rng.gamma(shape=shape, scale=scale)
    samples.append(float(sample))

print(samples)
