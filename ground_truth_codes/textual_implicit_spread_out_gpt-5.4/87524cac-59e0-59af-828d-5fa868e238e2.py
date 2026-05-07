import numpy as np

a = 2
b = 30
c = 11
samples = []

for _ in range(10000):
    u = np.random.rand()
    fc = (c - a) / (b - a)
    if u < fc:
        sample = a + np.sqrt(u * (b - a) * (c - a))
    else:
        sample = b - np.sqrt((1 - u) * (b - a) * (b - c))
    samples.append(float(sample))

print(samples)
