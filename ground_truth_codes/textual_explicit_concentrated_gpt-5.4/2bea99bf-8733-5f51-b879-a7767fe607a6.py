import numpy as np

rng = np.random.default_rng()
lam = 1.2
values = np.array([1, 2])
probs = np.array([0.8, 0.2])

samples = []

for _ in range(10000):
    N = rng.poisson(lam)
    if N == 0:
        sample = 0
    else:
        X = rng.choice(values, size=N, p=probs)
        sample = int(X.sum())
    samples.append(sample)

print(samples)
