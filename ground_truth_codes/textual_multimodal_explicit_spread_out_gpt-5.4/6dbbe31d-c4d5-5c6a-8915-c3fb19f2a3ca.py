import numpy as np

weights = [0.5, 0.5]
components = [(60, 0.2), (60, 0.8)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    n, p = components[chosen]
    sample = np.random.binomial(n, p)
    samples.append(sample)

print(samples)
