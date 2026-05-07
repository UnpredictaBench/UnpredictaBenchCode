import numpy as np
from scipy.stats import f

weights = [0.5, 0.5]
components = [(12, 40), (40, 12)]
samples = []

for _ in range(10000):
    idx = np.random.choice([0, 1], p=weights)
    d1, d2 = components[idx]
    sample = f.rvs(d1, d2)
    samples.append(float(sample))

print(samples)
