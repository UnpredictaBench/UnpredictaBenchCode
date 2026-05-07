import numpy as np
from scipy.stats import f

d1 = 2
d2 = 3
samples = []

for _ in range(10000):
    sample = f.rvs(dfn=d1, dfd=d2)
    samples.append(float(sample))

print(samples)
