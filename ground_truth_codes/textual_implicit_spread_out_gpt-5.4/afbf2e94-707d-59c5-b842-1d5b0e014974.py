import numpy as np

mu = np.array([12.0, -8.0, 20.0])
Sigma = np.array([
    [25.0, 12.0, 6.0],
    [12.0, 36.0, 10.0],
    [6.0, 10.0, 49.0]
])

samples = []
for _ in range(10000):
    sample = np.random.multivariate_normal(mean=mu, cov=Sigma)
    samples.append(float(sample[0]))

print(samples)
