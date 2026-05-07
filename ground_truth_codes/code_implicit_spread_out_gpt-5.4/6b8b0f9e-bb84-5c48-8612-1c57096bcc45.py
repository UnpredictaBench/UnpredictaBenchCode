import numpy as np

level = 6.8
shape = 0.55
samples = []

for _ in range(10000):
    v = np.random.normal()
    y = v * v
    x = level + (level * level * y) / (2 * shape) - (level / (2 * shape)) * np.sqrt(4 * level * shape * y + (level * level) * (y * y))
    u = np.random.uniform()
    sample = x if u <= level / (level + x) else (level * level) / x
    samples.append(float(sample))

print(samples)
