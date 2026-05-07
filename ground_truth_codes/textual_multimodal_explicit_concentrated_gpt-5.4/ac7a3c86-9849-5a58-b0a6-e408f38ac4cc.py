import numpy as np

means = [-0.8, 0.8]
stds = [0.12, 0.12]
weights = [0.5, 0.5]

samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.normal(loc=means[component], scale=stds[component])
    samples.append(float(sample))

print(samples)
