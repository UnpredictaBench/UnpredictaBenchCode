import numpy as np

r = 3
p = 0.85

samples = []
for _ in range(10000):
    sample = np.random.negative_binomial(r, p)
    samples.append(sample)

print(samples)
