import numpy as np
from scipy.stats import invweibull

alpha = 8.0
s = 0.4
m = 10.0

samples = []
for _ in range(10000):
    sample = invweibull.rvs(c=alpha, loc=m, scale=s)
    samples.append(float(sample))

print(samples)
