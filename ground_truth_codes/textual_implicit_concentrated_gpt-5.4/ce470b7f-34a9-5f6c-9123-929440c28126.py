import numpy as np

lam = 1.4
samples = []

for _ in range(10000):
    sample = np.random.poisson(lam=lam)
    samples.append(sample)

print(samples)
