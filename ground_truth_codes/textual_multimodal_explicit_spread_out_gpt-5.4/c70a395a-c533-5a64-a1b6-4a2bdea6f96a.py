import numpy as np

weights = [0.35, 0.65]
mus = [-1.2, 2.4]
sigmas = [1.1, 0.9]

samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.lognormal(mean=mus[component], sigma=sigmas[component])
    samples.append(sample)

print(samples)
