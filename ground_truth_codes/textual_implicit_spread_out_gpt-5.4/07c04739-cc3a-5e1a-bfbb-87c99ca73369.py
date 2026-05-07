import numpy as np

samples = []
r = 12

for _ in range(10000):
    u = np.random.uniform(0, 2 * np.pi)
    sample = r * np.cos(u)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
