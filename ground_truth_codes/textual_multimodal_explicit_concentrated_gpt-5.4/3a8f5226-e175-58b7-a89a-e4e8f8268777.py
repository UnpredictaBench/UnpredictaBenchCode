import numpy as np

weights = [0.5, 0.5]
ps = [0.1, 0.9]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.binomial(1, ps[component])
    samples.append(sample)

print(samples)
