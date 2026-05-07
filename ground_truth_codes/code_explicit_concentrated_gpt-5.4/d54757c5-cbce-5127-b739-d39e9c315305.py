import numpy as np

# F-distribution parameters (degrees of freedom)
d1 = 50.0
d2 = 60.0

samples = []

for _ in range(10000):
    sample = np.random.f(d1, d2)
    samples.append(sample)

print(samples)
