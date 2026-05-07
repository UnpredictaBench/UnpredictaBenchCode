import numpy as np
from scipy.stats import skellam

weights = [0.5, 0.5]
components = [(0.4, 2.0), (2.0, 0.4)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    mu1, mu2 = components[chosen]
    sample = skellam.rvs(mu1, mu2)
    samples.append(int(sample))

print(samples)
