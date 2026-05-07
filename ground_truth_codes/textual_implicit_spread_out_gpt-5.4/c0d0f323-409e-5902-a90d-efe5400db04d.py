import numpy as np

n = 120
p = 0.5
samples = []

for _ in range(10000):
    sample = np.random.binomial(n=n, p=p)
    samples.append(sample)

print(samples)
