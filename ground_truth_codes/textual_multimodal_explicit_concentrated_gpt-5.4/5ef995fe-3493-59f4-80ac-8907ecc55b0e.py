import numpy as np

weights = [0.5, 0.5]
components = [(1.0, 1.3), (1.8, 2.1)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    a, b = components[chosen]
    sample = np.exp(np.random.uniform(np.log(a), np.log(b)))
    samples.append(float(sample))

print(samples)
