import numpy as np

sigmas = [0.35, 1.1]
weights = [0.5, 0.5]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.rayleigh(scale=sigmas[component])
    samples.append(sample)

print(samples)
