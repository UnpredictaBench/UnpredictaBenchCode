import numpy as np

mu = 0.2
s = 0.15
samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = mu + s * np.log(u / (1.0 - u))
    samples.append(float(sample))

print(samples)
