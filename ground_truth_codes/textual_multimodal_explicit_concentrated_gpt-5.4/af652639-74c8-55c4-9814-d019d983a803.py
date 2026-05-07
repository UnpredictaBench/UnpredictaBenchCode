import numpy as np

weights = [0.5, 0.5]
mus = [-0.35, 0.42]
sigmas = [0.08, 0.07]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    s = np.random.normal(loc=mus[k], scale=sigmas[k])
    x = max(0.0, s)
    samples.append(x)

print(samples)
