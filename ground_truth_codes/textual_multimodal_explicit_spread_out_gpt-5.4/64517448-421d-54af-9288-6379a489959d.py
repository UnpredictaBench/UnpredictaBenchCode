import numpy as np

weights = [0.5, 0.5]
ranges = [(1, 40), (81, 120)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    a, b = ranges[chosen]
    sample = np.random.randint(a, b + 1)
    samples.append(sample)

print(samples)
