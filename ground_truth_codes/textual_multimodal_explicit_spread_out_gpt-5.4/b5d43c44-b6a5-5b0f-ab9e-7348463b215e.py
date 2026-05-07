import numpy as np

weights = [0.5, 0.5]
params = [(-18, 14), (32, 16)]
samples = []

for _ in range(10000):
    comp = np.random.choice([0, 1], p=weights)
    mu, sigma = params[comp]
    s = np.random.normal(mu, sigma)
    x = max(0.0, s)
    samples.append(x)

print(samples)
