import numpy as np

# F-distribution parameters (degrees of freedom)
d1 = 2.5
d2 = 3.5

samples = []

for _ in range(10000):
    sample = np.random.f(dfnum=d1, dfden=d2)
    samples.append(sample)

print(samples)
