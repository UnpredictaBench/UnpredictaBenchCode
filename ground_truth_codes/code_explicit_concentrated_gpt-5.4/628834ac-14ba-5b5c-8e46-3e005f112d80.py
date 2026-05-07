import numpy as np

# Fréchet distribution parameters
alpha = 8.0   # shape > 0
s = 0.7       # scale > 0
m = 1.5       # location

samples = []

for _ in range(10000):
    u = np.random.uniform(0.0, 1.0)
    sample = m + s * (-np.log(u)) ** (-1.0 / alpha)
    samples.append(float(sample))

print(samples)
