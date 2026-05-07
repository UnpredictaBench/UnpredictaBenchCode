import numpy as np

mu = 0.15
sigma = 0.2
samples = []

for _ in range(10000):
    z = np.random.normal(0.0, 1.0)
    sample = np.exp(mu + sigma * z)
    samples.append(float(sample))

print(samples)
