import numpy as np
from scipy.stats import erlang

k = 2
lambda_ = 0.35
scale = 1 / lambda_

samples = []
for _ in range(10000):
    sample = erlang.rvs(a=k, scale=scale)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
