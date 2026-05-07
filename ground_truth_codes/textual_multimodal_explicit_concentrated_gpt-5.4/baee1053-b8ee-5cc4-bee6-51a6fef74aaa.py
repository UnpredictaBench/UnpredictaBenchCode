import numpy as np

weights = np.array([0.5, 0.5])
intervals = [(0.0, 0.18), (0.82, 1.0)]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    a, b = intervals[k]
    u = np.random.random()
    sample = a + (b - a) * (np.sin(np.pi * u / 2) ** 2)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
