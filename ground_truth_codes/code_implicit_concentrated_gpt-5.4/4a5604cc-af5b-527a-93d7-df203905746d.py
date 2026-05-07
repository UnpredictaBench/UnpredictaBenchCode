import numpy as np

chance = 0.97
samples = []

for _ in range(10000):
    sample = int(np.random.random() < chance)
    samples.append(sample)

print(samples)
