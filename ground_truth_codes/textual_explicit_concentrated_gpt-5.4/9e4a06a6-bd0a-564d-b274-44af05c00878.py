import numpy as np

alpha = 8.0
s = 0.4
m = 1.2

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = m + s * (-np.log(u))**(-1.0 / alpha)
    samples.append(float(sample))

print(samples)
