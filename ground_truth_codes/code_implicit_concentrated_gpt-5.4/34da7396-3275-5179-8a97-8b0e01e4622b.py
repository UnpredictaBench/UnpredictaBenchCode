import numpy as np

floor = 10.0
shape = 25.0
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = floor / (u ** (1.0 / shape))
    samples.append(float(sample))

print(samples)
