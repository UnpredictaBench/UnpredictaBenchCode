import numpy as np

sigma = 6.5
n = 2.8
samples = []

for _ in range(10000):
    r = np.random.rayleigh(scale=sigma)
    x = np.random.exponential(scale=r / n)
    samples.append(x)

print(samples)
