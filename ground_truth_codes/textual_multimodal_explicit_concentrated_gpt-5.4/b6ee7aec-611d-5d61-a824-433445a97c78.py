import numpy as np

mus = np.array([-0.9, 0.9])
scales = np.array([0.18, 0.18])
weights = np.array([0.5, 0.5])

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    sample = np.random.logistic(loc=mus[k], scale=scales[k])
    samples.append(sample)

print(samples)
