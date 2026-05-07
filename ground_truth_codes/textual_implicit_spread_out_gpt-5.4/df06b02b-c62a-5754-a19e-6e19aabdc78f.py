import numpy as np

a = 0.001
b = 1000.0
samples = []

for _ in range(10000):
    sample = np.exp(np.random.uniform(np.log(a), np.log(b)))
    samples.append(float(sample))

print(samples)
