import numpy as np

mu = 1.0
lam = 40.0
samples = []

for _ in range(10000):
    sample = np.random.wald(mean=mu, scale=lam)
    samples.append(float(sample))

print(samples)
