import numpy as np

a = 0.001
b = 1000.0
samples = []

for _ in range(10000):
    u = np.random.uniform(np.log(a), np.log(b))
    sample = float(np.exp(u))
    samples.append(sample)

print(samples)
