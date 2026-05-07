import numpy as np

rng = np.random.default_rng()
lam = 12.5
alpha = 2.3
beta = 0.4  # rate
results = []

for _ in range(10000):
    N = rng.poisson(lam)
    if N == 0:
        Y = 0.0
    else:
        X = rng.gamma(shape=alpha, scale=1.0/beta, size=N)
        Y = float(X.sum())
    results.append(Y)

print(results)
