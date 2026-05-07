import numpy as np

x_m = 2.5
alpha = 0.65
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = x_m / (u ** (1.0 / alpha))
    samples.append(float(sample))

print(samples)
