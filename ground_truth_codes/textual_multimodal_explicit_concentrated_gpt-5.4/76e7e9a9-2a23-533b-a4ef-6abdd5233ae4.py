import numpy as np
from scipy.stats import truncnorm

samples = []
weights = [0.5, 0.5]

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)

    if chosen == 0:
        mu, sigma, a, b = -1.2, 0.18, -1.6, -0.8
    else:
        mu, sigma, a, b = 1.1, 0.16, 0.8, 1.4

    alpha = (a - mu) / sigma
    beta = (b - mu) / sigma
    sample = truncnorm.rvs(alpha, beta, loc=mu, scale=sigma)
    samples.append(float(sample))

print(samples)
