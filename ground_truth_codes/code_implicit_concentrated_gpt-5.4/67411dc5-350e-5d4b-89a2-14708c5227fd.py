import numpy as np

samples = []
center = 0.15
steepness = 0.08

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = center + steepness * np.log(u / (1.0 - u))
    samples.append(float(sample))

print(samples)
