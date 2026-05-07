import numpy as np

weights = [0.45, 0.55]
components = [(3, 0.18), (14, 0.82)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    r, p = components[chosen]
    sample = np.random.negative_binomial(r, p)
    samples.append(sample)

print(samples)
