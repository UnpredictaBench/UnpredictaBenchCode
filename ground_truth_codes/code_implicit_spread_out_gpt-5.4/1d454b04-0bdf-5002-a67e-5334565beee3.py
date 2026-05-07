import numpy as np

rate_per_minute = 0.08
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = -np.log(u) / rate_per_minute
    samples.append(float(sample))

print(samples)
