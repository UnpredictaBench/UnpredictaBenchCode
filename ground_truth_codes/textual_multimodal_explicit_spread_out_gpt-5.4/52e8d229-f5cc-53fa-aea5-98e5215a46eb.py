import numpy as np

weights = [0.5, 0.5]
components = [(0.001, 1.0), (1000.0, 1000000.0)]

samples = []
for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    a, b = components[k]
    u = np.random.uniform(np.log(a), np.log(b))
    sample = np.exp(u)
    samples.append(float(sample))  # Convert np.float64 to float for valid Python literal

print(samples)
