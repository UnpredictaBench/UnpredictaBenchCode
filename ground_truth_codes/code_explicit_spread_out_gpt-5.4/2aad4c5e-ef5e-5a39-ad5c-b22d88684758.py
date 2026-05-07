import numpy as np

# Triangular distribution parameters
left = -120.0   # a
mode = 30.0     # c
right = 180.0   # b

samples = []

for _ in range(10000):
    sample = np.random.triangular(left, mode, right)
    samples.append(sample)

print(samples)
