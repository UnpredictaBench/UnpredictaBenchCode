import numpy as np

weights = [0.5, 0.5]
components = [(1, 2), (5, 6)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    a, b = components[chosen]
    sample = np.random.randint(a, b + 1)
    samples.append(sample)

print(samples)
