import numpy as np

# Beta-binomial sampling via its compound representation:
# first draw p ~ Beta(alpha, beta), then draw X ~ Binomial(n, p)

rng = np.random.default_rng()

n = 8
alpha = 40.0
beta = 42.0

samples = []

for _ in range(10000):
    p = rng.beta(alpha, beta)
    sample = rng.binomial(n, p)
    samples.append(sample)

print(samples)
