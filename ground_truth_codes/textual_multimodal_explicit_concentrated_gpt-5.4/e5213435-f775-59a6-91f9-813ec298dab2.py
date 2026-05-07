import numpy as np

weights = [0.55, 0.45]
params = [(1.0, 18.0), (1.8, 22.0)]  # (xm, alpha)

samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    xm, alpha = params[chosen]
    u = np.random.uniform(0.0, 1.0)
    sample = xm / (u ** (1.0 / alpha))
    samples.append(sample)

print(samples)
