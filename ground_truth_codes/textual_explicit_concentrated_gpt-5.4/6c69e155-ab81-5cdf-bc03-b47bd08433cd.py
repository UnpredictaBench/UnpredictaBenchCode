import numpy as np

a = 0.45
b = 0.55
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = (b - a) * (np.sin(np.pi * u / 2) ** 2) + a
    samples.append(float(sample))

print(samples)
