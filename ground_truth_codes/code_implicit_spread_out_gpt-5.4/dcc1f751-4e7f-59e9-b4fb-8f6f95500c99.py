import numpy as np

samples = []
center = 4.8
stretch = 9.7

for _ in range(10000):
    u = np.random.uniform(1e-12, 1 - 1e-12)
    value = center + stretch * np.log(u / (1 - u))
    samples.append(float(value))

print(samples)
