import numpy as np

weights = [0.5, 0.5]
params = [(0.9, 18.0), (1.3, 26.0)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    mu, lam = params[chosen]
    sample = np.random.wald(mu, lam)
    samples.append(sample)

print(samples)
