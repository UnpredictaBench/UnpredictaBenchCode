import numpy as np

left = 0.42
right = 0.58
samples = []

for _ in range(10000):
    angle = np.random.uniform(0.0, 2.0 * np.pi)
    sample = left + (right - left) * (np.sin(angle) ** 2)
    samples.append(float(sample))

print(samples)
