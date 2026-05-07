import numpy as np

a = -100.0
b = 100.0

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = a + (b - a) * np.sin(np.pi * u / 2.0) ** 2
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
