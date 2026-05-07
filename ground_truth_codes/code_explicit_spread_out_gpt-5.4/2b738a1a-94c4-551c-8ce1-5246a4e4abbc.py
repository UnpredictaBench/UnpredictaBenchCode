import numpy as np

# Erlang distribution parameters
k = 9          # shape (positive integer)
lambda_rate = 0.35  # rate (positive real)

samples = []

for _ in range(10000):
    sample = np.random.gamma(shape=k, scale=1.0/lambda_rate)
    samples.append(sample)

print(samples)
