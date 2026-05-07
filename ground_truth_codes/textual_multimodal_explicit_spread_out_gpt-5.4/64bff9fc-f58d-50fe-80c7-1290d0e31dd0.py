import numpy as np

weights = [0.5, 0.5]
results = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)

    if component == 0:
        lam = 2.0
        rate = 0.25
    else:
        lam = 9.0
        rate = 1.8

    N = np.random.poisson(lam)
    if N == 0:
        Y = 0.0
    else:
        Y = np.random.exponential(scale=1.0/rate, size=N).sum()

    results.append(float(Y))

print(results)
