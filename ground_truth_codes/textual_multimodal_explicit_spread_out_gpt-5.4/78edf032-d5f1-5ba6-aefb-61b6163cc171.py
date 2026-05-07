import numpy as np

weights = [0.5, 0.5]
components = [(2, 0.2), (7, 1.4)]  # (k, lambda)
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    k, lam = components[chosen]
    sample = np.random.gamma(shape=k, scale=1.0/lam)
    samples.append(sample)

print(samples)
