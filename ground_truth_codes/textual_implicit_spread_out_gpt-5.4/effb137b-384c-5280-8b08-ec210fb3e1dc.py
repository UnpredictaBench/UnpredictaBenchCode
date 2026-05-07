import numpy as np

a = 120
b = 980
samples = []

for _ in range(10000):
    sample = np.random.randint(a, b + 1)
    samples.append(sample)

print(samples)
