import numpy as np

p = np.array([0.08, 0.15, 0.22, 0.31, 0.39, 0.47, 0.53, 0.61, 0.69, 0.78, 0.85, 0.92])

rng = np.random.default_rng()
samples = []

for _ in range(10000):
    sample = rng.binomial(n=1, p=p).sum()
    samples.append(int(sample))

print(samples)
