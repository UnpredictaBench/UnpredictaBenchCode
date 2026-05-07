import numpy as np

p = 0.08
samples = []

for _ in range(10000):
    sample = np.random.geometric(p) - 1
    samples.append(sample)

print(samples)
