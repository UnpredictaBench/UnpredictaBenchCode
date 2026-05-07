import numpy as np

weights = [0.5, 0.5]
mus = [-0.2, 0.35]
sigmas = [0.12, 0.10]

samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.lognormal(mean=mus[component], sigma=sigmas[component])
    samples.append(sample)

print(samples)
