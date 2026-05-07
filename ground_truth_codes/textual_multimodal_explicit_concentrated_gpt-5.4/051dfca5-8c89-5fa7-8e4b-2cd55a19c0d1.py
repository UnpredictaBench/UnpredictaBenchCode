import numpy as np

weights = [0.5, 0.5]
means = [np.array([0.0, 0.0]), np.array([0.8, 0.8])]
covs = [np.array([[0.04, 0.0], [0.0, 0.04]]), np.array([[0.03, 0.0], [0.0, 0.03]])]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    sample = np.random.multivariate_normal(means[k], covs[k])
    samples.append(float(sample[0]))

print(samples)
