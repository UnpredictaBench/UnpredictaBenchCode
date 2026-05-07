import numpy as np

k = 4
p = [0.82, 0.10, 0.05, 0.03]
samples = []

for _ in range(10000):
    sample = np.random.choice(np.arange(1, k + 1), p=p)
    samples.append(int(sample))  # Convert np.int64 to int

print(samples)
