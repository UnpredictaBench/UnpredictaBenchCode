import numpy as np

mu = np.array([0.05, -0.02])
Sigma = np.array([[0.04, 0.01], [0.01, 0.03]])

samples = []

for _ in range(10000):
    sample = np.random.multivariate_normal(mean=mu, cov=Sigma)
    samples.append(float(sample[0]))

print(samples)
