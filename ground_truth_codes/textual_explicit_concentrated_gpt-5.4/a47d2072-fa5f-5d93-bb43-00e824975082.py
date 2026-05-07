import numpy as np
from scipy.stats import triang

a = 0.20
b = 0.50
c = 0.32
shape = (c - a) / (b - a)

samples = []
for _ in range(10000):
    sample = triang.rvs(shape, loc=a, scale=b-a, size=1)[0]
    samples.append(float(sample))

print(samples)
