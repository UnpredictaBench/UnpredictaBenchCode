import numpy as np

mus = [-18, 22]
scales = [6, 7]
weights = [0.5, 0.5]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    sample = np.random.logistic(loc=mus[k], scale=scales[k])
    samples.append(sample)

print(samples)
