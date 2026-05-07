import numpy as np

p = 0.03
samples = []

for _ in range(10000):
    sample = np.random.binomial(n=1, p=p)
    samples.append(sample)

print(samples)
