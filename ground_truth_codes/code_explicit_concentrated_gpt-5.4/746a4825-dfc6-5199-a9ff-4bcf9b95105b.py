import numpy as np

# Gumbel distribution parameters
mu = 0.2
beta = 0.3

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = mu - beta * np.log(-np.log(u))
    samples.append(float(sample))

print(samples)
