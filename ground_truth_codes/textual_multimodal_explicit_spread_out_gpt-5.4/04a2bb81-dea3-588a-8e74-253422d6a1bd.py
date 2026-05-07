import numpy as np

weights = [0.5, 0.5]
sigmas = [2.5, 11.0]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.rayleigh(scale=sigmas[component])
    samples.append(sample)

print(samples)
