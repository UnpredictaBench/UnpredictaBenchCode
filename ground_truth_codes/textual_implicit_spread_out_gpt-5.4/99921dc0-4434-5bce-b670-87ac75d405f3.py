import numpy as np
from scipy.stats import erlang

k = 8
lambda_ = 0.15
samples = []

for _ in range(10000):
    sample = erlang.rvs(a=k, scale=1/lambda_)
    samples.append(float(sample))

print(samples)
