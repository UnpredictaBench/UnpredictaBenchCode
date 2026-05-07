import numpy as np

# Beta distribution parameters
alpha = 50.0
beta = 50.0

samples = []

for _ in range(10000):
    sample = np.random.beta(alpha, beta)
    samples.append(sample)

print(samples)
