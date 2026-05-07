import numpy as np

weights = [0.5, 0.5]
components = [
    [0.30, 0.25, 0.20, 0.15, 0.07, 0.03],
    [0.03, 0.07, 0.15, 0.20, 0.25, 0.30]
]
categories = np.array([1, 2, 3, 4, 5, 6])

samples = []
for _ in range(10000):
    comp = np.random.choice([0, 1], p=weights)
    sample = int(np.random.choice(categories, p=components[comp]))
    samples.append(sample)

print(samples)
