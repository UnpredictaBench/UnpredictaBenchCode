import numpy as np

rng = np.random.default_rng()
scale = 0.35
component_loc = 0.8
component_sd = 0.12

samples = []

for _ in range(10000):
    radius = rng.rayleigh(scale=scale)
    sample = rng.normal(loc=component_loc + 0.5 * radius, scale=component_sd)
    samples.append(float(sample))

print(samples)
