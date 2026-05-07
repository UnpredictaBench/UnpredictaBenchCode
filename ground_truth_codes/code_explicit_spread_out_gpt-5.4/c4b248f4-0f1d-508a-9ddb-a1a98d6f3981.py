import numpy as np

a = -500
b = 500
samples = []

for _ in range(10000):
    sample = np.random.randint(a, b + 1)
    samples.append(sample)

print(samples)
