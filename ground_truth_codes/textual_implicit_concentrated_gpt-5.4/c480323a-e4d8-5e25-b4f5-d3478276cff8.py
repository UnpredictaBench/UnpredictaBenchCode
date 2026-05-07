import numpy as np
from scipy.stats import triang

a = 4.8
b = 5.4
c = 5.1
shape = (c - a) / (b - a)

samples = []
for _ in range(10000):
    sample = triang.rvs(shape, loc=a, scale=b-a)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
