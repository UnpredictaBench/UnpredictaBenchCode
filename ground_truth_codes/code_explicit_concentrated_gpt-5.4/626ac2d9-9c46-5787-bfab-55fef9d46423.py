import numpy as np

samples = []

for _ in range(10000):
    U = np.random.uniform(0.0, 1.0)
    sample = np.sin(np.pi * U / 2.0) ** 2
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
