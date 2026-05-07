import numpy as np

# Triangular distribution parameters
left = 0.0
mode = 0.08
right = 0.12

samples = []

for _ in range(10000):
    sample = np.random.triangular(left, mode, right)
    samples.append(sample)

print(samples)
