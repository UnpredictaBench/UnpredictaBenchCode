import numpy as np

shape = 0.7
scale = 9.5
samples = []

for _ in range(10000):
    u = np.random.random()
    boosted = np.random.gamma(shape + 1.0, scale)
    sample = boosted * (u ** (1.0 / shape))
    samples.append(float(sample))

print(samples)
