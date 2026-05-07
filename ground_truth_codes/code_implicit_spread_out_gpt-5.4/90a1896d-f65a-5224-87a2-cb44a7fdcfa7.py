import numpy as np

arrival_rate = 9.4
shape = 1.3
scale = 8.7
totals = []

for _ in range(10000):
    rng = np.random.default_rng()
    count = rng.poisson(arrival_rate)
    if count == 0:
        total = 0.0
    else:
        pieces = rng.gamma(shape=shape, scale=scale, size=count)
        total = float(np.sum(pieces))
    totals.append(total)

print(totals)
