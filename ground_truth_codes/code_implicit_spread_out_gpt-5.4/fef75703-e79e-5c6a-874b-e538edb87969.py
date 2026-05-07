import numpy as np

rng = np.random.default_rng()
hit_chance = 0.12
samples = []

for _ in range(10000):
    sample = rng.random()
    samples.append(sample)

print(samples)
