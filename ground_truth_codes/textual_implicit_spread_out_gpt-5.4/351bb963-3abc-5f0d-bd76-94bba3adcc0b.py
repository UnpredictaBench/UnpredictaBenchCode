import numpy as np

sigma = 3.8
rng = np.random.default_rng()
samples = []

for _ in range(10000):
    R = rng.rayleigh(scale=sigma)
    X = rng.normal(loc=0.0, scale=R)
    samples.append(float(X))

print(samples)
