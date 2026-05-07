import numpy as np

locations = [-18, 22]
scales = [9, 11]
weights = [0.5, 0.5]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    sample = np.random.laplace(loc=locations[chosen], scale=scales[chosen])
    samples.append(sample)

print(samples)
