import numpy as np

rate = 4.8
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = -np.log(u) / rate
    samples.append(float(sample))

print(samples)
