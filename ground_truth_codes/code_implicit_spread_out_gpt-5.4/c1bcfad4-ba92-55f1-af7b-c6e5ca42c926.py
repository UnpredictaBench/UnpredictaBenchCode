import numpy as np

rng = np.random.default_rng()
shape = 0.62
scale = 18.0
floor = -7.5
samples = []

for _ in range(10000):
    u = rng.uniform()
    sample = floor + scale * (-np.log(u)) ** (-1.0 / shape)
    samples.append(float(sample))

print(samples)
