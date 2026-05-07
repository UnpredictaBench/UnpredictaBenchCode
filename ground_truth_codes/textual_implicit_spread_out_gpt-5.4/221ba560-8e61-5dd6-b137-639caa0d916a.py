import numpy as np

k = 7
p = np.array([0.14, 0.16, 0.12, 0.18, 0.10, 0.15, 0.15])
samples = []

for _ in range(10000):
    sample = np.random.choice(np.arange(1, k + 1), p=p)
    samples.append(int(sample))  # Convert np.int64 to int

print(samples)
