import numpy as np

n = 60
p = [0.24, 0.26, 0.25, 0.25]
samples = []

for _ in range(10000):
    sample = np.random.multinomial(n, p)
    samples.append(int(sample[0]))

print(samples)
