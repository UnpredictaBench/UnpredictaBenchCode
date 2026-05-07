import numpy as np
from scipy.stats import skellam

weights = [0.5, 0.5]
components = [(4, 28), (30, 3)]
samples = []

for _ in range(10000):
    chosen = np.random.choice([0, 1], p=weights)
    mu1, mu2 = components[chosen]
    sample = skellam.rvs(mu1, mu2)
    samples.append(int(sample))

print(samples)
