import numpy as np

lambda_rate = 0.12
samples = []

for _ in range(10000):
    sample = np.random.exponential(scale=1/lambda_rate)
    samples.append(sample)

print(samples)
