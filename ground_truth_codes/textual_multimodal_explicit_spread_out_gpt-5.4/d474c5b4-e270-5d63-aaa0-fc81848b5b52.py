import numpy as np

weights = [0.45, 0.55]
means = [np.array([-18.0, 22.0]), np.array([27.0, -16.0])]
covs = [np.array([[36.0, 14.0], [14.0, 49.0]]),
        np.array([[64.0, -20.0], [-20.0, 81.0]])]

samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.multivariate_normal(means[component], covs[component])
    samples.append(float(sample[0]))

print(samples)
