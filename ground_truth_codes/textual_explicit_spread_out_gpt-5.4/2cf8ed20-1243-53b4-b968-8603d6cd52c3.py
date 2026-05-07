import numpy as np
from scipy.stats import triang

a = -50
b = 150
c = 40
loc = a
scale = b - a
shape = (c - a) / (b - a)

samples = []
for _ in range(10000):
    sample = triang.rvs(shape, loc=loc, scale=scale, size=1)[0]
    samples.append(float(sample))  # Convert np.float64 to regular float

print(samples)
