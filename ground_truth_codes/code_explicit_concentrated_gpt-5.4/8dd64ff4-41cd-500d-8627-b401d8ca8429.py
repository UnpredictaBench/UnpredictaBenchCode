import numpy as np

mu = np.array([0.15, -0.1])
Sigma = np.array([[0.04, 0.012],
                  [0.012, 0.09]])

samples = []
rng = np.random.default_rng()

for _ in range(10000):
    sample = rng.multivariate_normal(mean=mu, cov=Sigma, size=1)
    samples.append(float(sample[0, 0]))

print(samples)
