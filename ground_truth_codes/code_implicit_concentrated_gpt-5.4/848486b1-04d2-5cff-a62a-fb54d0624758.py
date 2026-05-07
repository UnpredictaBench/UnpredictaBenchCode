import numpy as np

low = 2.0
high = 2.6
samples = []

for _ in range(10000):
    u = np.random.uniform(np.log(low), np.log(high))
    sample = float(np.exp(u))
    samples.append(sample)

print(samples)
