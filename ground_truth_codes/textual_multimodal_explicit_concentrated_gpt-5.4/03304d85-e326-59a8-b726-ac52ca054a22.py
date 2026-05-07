import numpy as np

weights = [0.5, 0.5]
mus = [-1.2, 1.1]
betas = [0.18, 0.16]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    u = np.random.uniform(0.0, 1.0)
    sample = mus[k] - betas[k] * np.log(-np.log(u))
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
