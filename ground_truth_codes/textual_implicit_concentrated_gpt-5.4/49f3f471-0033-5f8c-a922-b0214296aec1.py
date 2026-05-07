import numpy as np

r = 0.5
samples = []

for _ in range(10000):
    theta = np.random.uniform(0, 2 * np.pi)
    X = r * np.cos(theta)
    S = (X + r) / (2 * r)
    samples.append(float(S))

print(samples)
