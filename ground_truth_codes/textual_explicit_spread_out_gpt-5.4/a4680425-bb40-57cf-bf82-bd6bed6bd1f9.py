import numpy as np

n = 30
p = [0.18, 0.22, 0.20, 0.25, 0.15]
samples = []

for _ in range(10000):
    sample = np.random.multinomial(n, p)
    samples.append(int(sample[3]))

print(samples)
