import numpy as np

alpha = np.array([25.0, 30.0, 28.0, 32.0])
samples = []

for _ in range(10000):
    sample = np.random.dirichlet(alpha)
    samples.append(float(sample[0]))

print(samples)
