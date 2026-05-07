import numpy as np

weights = [0.5, 0.5]
params = [(40, 10), (10, 40)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    a, b = params[chosen]
    sample = np.random.beta(a, b)
    samples.append(sample)

print(samples)
