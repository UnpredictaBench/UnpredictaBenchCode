import numpy as np

alpha = 0.85
s = 9.5
m = 12.0
samples = []

for _ in range(10000):
    u = np.random.uniform()
    sample = m + s * (-np.log(u))**(-1/alpha)
    samples.append(float(sample))

print(samples)
