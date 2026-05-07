import numpy as np

p = 0.08
samples = []

for _ in range(10000):
    u = np.random.random()
    sample = int(np.ceil(np.log(u) / np.log(1 - p)))
    samples.append(sample)

print(samples)
