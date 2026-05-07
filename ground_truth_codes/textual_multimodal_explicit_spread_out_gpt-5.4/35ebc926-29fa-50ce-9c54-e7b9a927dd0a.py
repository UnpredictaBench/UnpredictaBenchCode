import numpy as np

weights = [0.5, 0.5]
ps = [0.08, 0.65]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.geometric(ps[component])
    samples.append(int(sample))

print(samples)
