import numpy as np

p = np.array([0.08, 0.19, 0.27, 0.34, 0.41, 0.48, 0.55, 0.63, 0.71, 0.79, 0.86, 0.93])
samples = []

for _ in range(10000):
    sample = np.random.binomial(n=1, p=p).sum()
    samples.append(int(sample))

print(samples)
