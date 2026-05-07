import numpy as np

k = 3
p = [0.92, 0.06, 0.02]
samples = []

for _ in range(10000):
    sample = int(np.random.choice(np.arange(1, k + 1), p=p))
    samples.append(sample)

print(samples)
