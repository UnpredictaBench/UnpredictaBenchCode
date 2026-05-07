import numpy as np

weights = [0.35, 0.65]
components = [(1.5, 0.8), (60.0, 1.1)]  # (xm, alpha)
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    xm, alpha = components[chosen]
    u = np.random.uniform(0.0, 1.0)
    sample = xm / (u ** (1.0 / alpha))
    samples.append(float(sample))

print(samples)
