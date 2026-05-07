import numpy as np

mean = np.array([0.2, -0.1])
cov = np.array([[0.04, 0.01], [0.01, 0.03]])
samples = []

for _ in range(10000):
    sample = np.random.multivariate_normal(mean, cov)
    samples.append(float(sample[0]))

print(samples)
