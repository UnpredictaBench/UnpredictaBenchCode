import numpy as np

weights = [0.5, 0.5]
components = [(0.5, 3.0), (3.0, 0.5)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    a, b = components[chosen]
    sample = np.random.beta(a, b)
    samples.append(sample)

print(samples)
