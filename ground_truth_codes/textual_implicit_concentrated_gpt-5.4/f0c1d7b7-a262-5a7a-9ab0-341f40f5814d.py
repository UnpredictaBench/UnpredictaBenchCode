import numpy as np

a = 1.8
b = 2.4
samples = []

for _ in range(10000):
    u = np.random.uniform(np.log(a), np.log(b))
    sample = float(np.exp(u))
    samples.append(sample)

print(samples)
