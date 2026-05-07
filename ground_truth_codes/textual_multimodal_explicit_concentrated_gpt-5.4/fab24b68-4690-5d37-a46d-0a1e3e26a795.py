import numpy as np

locations = np.array([-0.8, 0.8])
scales = np.array([0.12, 0.12])
weights = np.array([0.5, 0.5])

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    sample = np.random.laplace(loc=locations[k], scale=scales[k])
    samples.append(float(sample))

print(samples)
