import numpy as np
from scipy.stats import erlang

k = 2
lam = 12
samples = []

for _ in range(10000):
    sample = erlang.rvs(a=k, scale=1/lam)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
