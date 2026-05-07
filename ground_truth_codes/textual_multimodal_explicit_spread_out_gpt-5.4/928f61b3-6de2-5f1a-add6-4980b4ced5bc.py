import numpy as np

means = [-30, 35]
stds = [12, 18]
weights = [0.45, 0.55]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.normal(means[component], stds[component])
    samples.append(float(sample))

print(samples)
