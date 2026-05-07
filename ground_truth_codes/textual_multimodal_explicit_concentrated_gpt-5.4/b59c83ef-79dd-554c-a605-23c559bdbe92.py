import numpy as np

weights = [0.5, 0.5]
ps = [0.85, 0.25]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.geometric(ps[component])
    samples.append(sample)

print(samples)
