import numpy as np

a = 2.0
b = 2.5
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = a * (b / a) ** u
    samples.append(sample)

print(samples)
