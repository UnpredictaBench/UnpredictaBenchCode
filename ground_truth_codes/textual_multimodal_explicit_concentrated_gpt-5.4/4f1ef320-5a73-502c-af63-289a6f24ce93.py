import numpy as np

weights = [0.5, 0.5]
components = [
    [0.08, 0.10, 0.12, 0.09],
    [0.88, 0.90, 0.92, 0.89]
]

samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    ps = np.array(components[chosen])
    sample = np.random.binomial(1, ps).sum()
    samples.append(int(sample))

print(samples)
