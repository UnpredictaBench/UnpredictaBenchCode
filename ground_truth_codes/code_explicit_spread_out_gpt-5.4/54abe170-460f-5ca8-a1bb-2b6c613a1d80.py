import numpy as np

r = 2
p = 0.15

samples = []
for _ in range(10000):
    sample = np.random.negative_binomial(r, p)
    samples.append(sample)

print(samples)
