import numpy as np

weights = [0.35, 0.65]
components = [(1.2, 2.0), (9.0, 4.5)]  # (alpha, theta)
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    alpha, theta = components[chosen]
    sample = np.random.gamma(shape=alpha, scale=theta)
    samples.append(sample)

print(samples)
