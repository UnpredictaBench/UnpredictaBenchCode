import numpy as np

samples = []
left = -12.0
right = 12.0

for _ in range(10000):
    angle = np.random.uniform(0.0, 2.0 * np.pi)
    sample = 0.5 * (left + right) + 0.5 * (right - left) * np.cos(angle)
    samples.append(float(sample))

print(samples)
