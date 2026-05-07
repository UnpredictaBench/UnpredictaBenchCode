import numpy as np

weights = [0.5, 0.5]
intervals = [(-120, -20), (35, 155)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    a, b = intervals[chosen]
    sample = np.random.uniform(a, b)
    samples.append(sample)

print(samples)
