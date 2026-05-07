import numpy as np

# Pareto Type I parameters
x_m = 1.0
alpha = 20.0

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = x_m / (u ** (1.0 / alpha))
    samples.append(sample)

print(samples)
