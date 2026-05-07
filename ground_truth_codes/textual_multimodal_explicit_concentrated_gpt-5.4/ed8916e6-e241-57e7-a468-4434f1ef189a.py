import numpy as np

weights = [0.5, 0.5]
components = [(18, 0.08), (42, 0.08)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    shape, scale = components[chosen]
    sample = np.random.gamma(shape=shape, scale=scale)
    samples.append(sample)

print(samples)
