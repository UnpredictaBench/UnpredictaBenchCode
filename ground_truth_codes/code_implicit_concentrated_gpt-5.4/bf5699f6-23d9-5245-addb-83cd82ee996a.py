import numpy as np

rng = np.random.default_rng()
center = 0.15
scale = 0.2
samples = []

for _ in range(10000):
    u = rng.uniform(-0.5, 0.5)
    sample = center - scale * np.sign(u) * np.log(1 - 2 * abs(u))
    samples.append(float(sample))

print(samples)
