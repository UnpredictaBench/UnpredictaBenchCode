import numpy as np

rng = np.random.default_rng()
probs = np.array([0.11, 0.19, 0.23, 0.17])
other = 1.0 - probs.sum()

samples = []

for _ in range(10000):
    u = rng.random()
    cumulative = 0.0
    for i, p in enumerate(probs):
        cumulative += p
        if u < cumulative:
            samples.append(i)
            break
    else:
        samples.append(len(probs))  # Append the index for 'other'

print(samples)
