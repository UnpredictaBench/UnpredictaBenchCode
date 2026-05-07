import numpy as np

low = 1e-6
high = 1e6
samples = []

for _ in range(10000):
    u = np.random.uniform(np.log(low), np.log(high))
    sample = np.exp(u)
    samples.append(float(sample))

print(samples)
