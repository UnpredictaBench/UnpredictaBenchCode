import numpy as np

p = 0.9
samples = []

for _ in range(10000):
    sample = np.random.geometric(p)
    samples.append(sample)

print(samples)
