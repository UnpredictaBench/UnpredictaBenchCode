import numpy as np

mu = 0.0
s = 0.25
samples = []

for _ in range(10000):
    u = np.random.uniform()
    sample = mu + s * np.log(u / (1 - u))
    samples.append(float(sample))

print(samples)
