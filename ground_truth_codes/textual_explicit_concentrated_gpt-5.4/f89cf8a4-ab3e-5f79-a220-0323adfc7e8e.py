import numpy as np
from scipy.stats import erlang

k = 3
lam = 4.5
samples = []

for _ in range(10000):
    sample = erlang.rvs(a=k, scale=1/lam)
    samples.append(float(sample))

print(samples)
