import numpy as np

weights = [0.4, 0.6]
components = [(1.5, 0.35), (18.0, 1.8)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    mu, lam = components[chosen]
    sample = np.random.wald(mu, lam)
    samples.append(float(sample))

print(samples)
