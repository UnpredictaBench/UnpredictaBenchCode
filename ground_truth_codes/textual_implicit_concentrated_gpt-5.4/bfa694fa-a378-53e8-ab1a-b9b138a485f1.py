import numpy as np
from scipy.stats import f

d1 = 60
d2 = 80
samples = []

for _ in range(10000):
    sample = f.rvs(dfn=d1, dfd=d2)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
