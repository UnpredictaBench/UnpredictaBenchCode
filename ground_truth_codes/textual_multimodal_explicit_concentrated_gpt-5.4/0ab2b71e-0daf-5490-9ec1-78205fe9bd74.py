import numpy as np

samples = []

for _ in range(10000):
    weights = [0.5, 0.5]
    component = np.random.choice([0, 1], p=weights)

    if component == 0:
        lam = 0.8
        rate = 12.0
    else:
        lam = 1.1
        rate = 3.0

    N = np.random.poisson(lam)
    if N == 0:
        Y = 0.0
    else:
        Y = np.random.exponential(scale=1.0/rate, size=N).sum()

    samples.append(float(Y))

print(samples)
