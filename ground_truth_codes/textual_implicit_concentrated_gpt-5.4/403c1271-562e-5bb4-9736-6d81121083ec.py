import numpy as np

lam = 0.8
scale = 1.2  # mean of exponential
samples = []

for _ in range(10000):
    N = np.random.poisson(lam)
    sample = 0.0 if N == 0 else np.random.exponential(scale=scale, size=N).sum()
    samples.append(float(sample))  # Ensure the sample is a float

print(samples)
