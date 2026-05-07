import numpy as np

# Beta-binomial sampling via its compound representation:
# p ~ Beta(alpha, beta)
# X ~ Binomial(n, p)

rng = np.random.default_rng()

n = 40
alpha = 0.8
beta = 0.8

samples = []

for _ in range(10000):
    p = rng.beta(alpha, beta)
    sample = rng.binomial(n, p)
    samples.append(sample)

print(samples)
