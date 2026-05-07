import numpy as np

# Parameters for Logistic(mu, s)
mu = -5.0
s = 12.0

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = mu + s * np.log(u / (1.0 - u))
    samples.append(float(sample))

print(samples)
