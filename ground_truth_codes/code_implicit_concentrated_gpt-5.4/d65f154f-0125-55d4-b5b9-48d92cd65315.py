import numpy as np

arrival_rate = 0.9
piece_shape = 2.0
piece_scale = 0.4
samples = []

for _ in range(10000):
    rng = np.random.default_rng()
    count = rng.poisson(arrival_rate)
    if count == 0:
        sample = 0.0
    else:
        sample = rng.gamma(shape=piece_shape * count, scale=piece_scale)
    samples.append(float(sample))

print(samples)
