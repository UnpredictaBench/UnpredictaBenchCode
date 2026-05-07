import numpy as np

# Compound Poisson sample: Y = sum_{i=1}^N X_i
rng = np.random.default_rng()

lam = 18.0          # Poisson rate
shape = 2.5         # Gamma shape for jump sizes
scale = 4.0         # Gamma scale for jump sizes

samples = []

for _ in range(10000):
    N = rng.poisson(lam)
    if N == 0:
        sample = 0.0
    else:
        jumps = rng.gamma(shape=shape, scale=scale, size=N)
        sample = float(np.sum(jumps))
    samples.append(sample)

print(samples)
