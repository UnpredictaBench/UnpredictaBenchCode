import numpy as np

mu = 2.5
sigma = 6.8
samples = []

for _ in range(10000):
    s = np.random.normal(loc=mu, scale=sigma)
    x = max(0.0, s)
    samples.append(x)

print(samples)
