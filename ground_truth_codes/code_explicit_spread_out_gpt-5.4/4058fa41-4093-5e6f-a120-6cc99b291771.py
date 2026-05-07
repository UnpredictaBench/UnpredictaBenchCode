import numpy as np

# Pareto Type I parameters
x_m = 0.5   # scale / minimum value
alpha = 0.6 # shape

samples = []

# Draw 1000 samples, one at a time
for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = x_m / (u ** (1.0 / alpha))
    samples.append(sample)

print(samples)
