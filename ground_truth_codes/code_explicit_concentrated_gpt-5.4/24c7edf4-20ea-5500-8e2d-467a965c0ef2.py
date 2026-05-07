import numpy as np

# Gamma distribution with shape alpha and scale theta
alpha = 8.0
theta = 0.15

samples = []
for _ in range(10000):
    sample = np.random.gamma(shape=alpha, scale=theta)
    samples.append(sample)

print(samples)
