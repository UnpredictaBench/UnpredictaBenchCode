import numpy as np

weights = [0.5, 0.5]
components = [(2, 8), (5, 2)]  # (k, lambda)
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    k, lam = components[chosen]
    sample = np.random.gamma(shape=k, scale=1/lam)
    samples.append(float(sample))

print(samples)
