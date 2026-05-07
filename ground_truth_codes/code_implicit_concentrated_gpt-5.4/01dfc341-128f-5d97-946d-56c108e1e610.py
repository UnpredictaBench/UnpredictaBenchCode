import numpy as np

rng = np.random.default_rng()
base_level = 2.4
variability = 0.18
samples = []

for _ in range(10000):
    u = rng.uniform(1e-12, 1 - 1e-12)
    sample = base_level - variability * np.log(-np.log(u))
    samples.append(float(sample))

print(samples)
