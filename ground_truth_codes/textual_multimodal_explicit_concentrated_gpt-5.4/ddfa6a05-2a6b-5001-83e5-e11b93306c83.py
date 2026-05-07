import numpy as np

weights = [0.55, 0.45]
rates = [8.0, 1.6]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    sample = np.random.exponential(scale=1.0 / rates[chosen])
    samples.append(sample)

print(samples)
