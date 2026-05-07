import numpy as np

a = -12
b = 18
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = a + (b - a) * np.sin(np.pi * u / 2.0) ** 2
    samples.append(float(sample))

print(samples)
