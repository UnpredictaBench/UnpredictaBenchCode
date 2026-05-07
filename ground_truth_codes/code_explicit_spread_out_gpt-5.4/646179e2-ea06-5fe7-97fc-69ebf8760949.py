import numpy as np

# Reciprocal (log-uniform) distribution parameters
lower = 1e-6
upper = 1e6

samples = []

for _ in range(10000):
    u = np.random.uniform(np.log(lower), np.log(upper))
    sample = float(np.exp(u))
    samples.append(sample)

print(samples)
