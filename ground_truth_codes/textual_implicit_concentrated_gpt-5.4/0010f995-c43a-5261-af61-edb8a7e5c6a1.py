import numpy as np

lambda_ = 12
samples = []

for _ in range(10000):
    sample = np.random.exponential(scale=1/lambda_)
    samples.append(sample)

print(samples)
