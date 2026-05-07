import numpy as np

rng = np.random.default_rng()
shape = 8.0
scale = 0.25
floor = 1.5
samples = []

for _ in range(10000):
    u = rng.uniform()
    sample = floor + scale * (-np.log(u)) ** (-1.0 / shape)
    samples.append(float(sample))

print(samples)
