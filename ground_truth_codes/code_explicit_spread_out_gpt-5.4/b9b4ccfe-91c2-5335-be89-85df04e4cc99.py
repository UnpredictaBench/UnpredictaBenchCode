import numpy as np

# Parameters for a Gumbel distribution (maximum case)
mu = 25.0
beta = 12.0

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = mu - beta * np.log(-np.log(u))
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
