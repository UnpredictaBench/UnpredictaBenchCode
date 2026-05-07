import numpy as np
from scipy.stats import f

weights = [0.5, 0.5]
components = [(2.5, 7.5), (18.0, 3.2)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    d1, d2 = components[chosen]
    sample = f.rvs(d1, d2)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
